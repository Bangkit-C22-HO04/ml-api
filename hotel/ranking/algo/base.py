from typing import Dict, Tuple
import tensorflow as tf
import numpy as np

from hotel.constants import HOTEL_LIST_PATH, TRAVEL_LIST_PATH


class HotelRankingModel(tf.keras.Model):
    def __init__(self):
        super().__init__()

        hotel_vocab, travel_vocab = self._load_vocab_data()

        # Compute embeddings for hotel id.
        self.hotel_embeddings = tf.keras.Sequential(
            [
                tf.keras.layers.StringLookup(vocabulary=hotel_vocab, mask_token=None),
                tf.keras.layers.Embedding(len(hotel_vocab) + 1, 128),
                tf.keras.layers.Dense(256, activation="tanh"),
            ]
        )

        # Compute embeddings for travel purpose.
        self.travel_embeddings = tf.keras.Sequential(
            [
                tf.keras.layers.StringLookup(vocabulary=travel_vocab, mask_token=None),
                tf.keras.layers.Embedding(len(travel_vocab) + 1, 128),
                tf.keras.layers.Dense(256, activation="tanh"),
            ]
        )

        # Compute embeddings for gender purpose.
        self.gender_embeddings = tf.keras.Sequential(
            [
                tf.keras.layers.Embedding(2, 128),
                tf.keras.layers.Dense(256, activation="tanh"),
            ]
        )

        # Compute embeddings for device purpose.
        self.device_embeddings = tf.keras.Sequential(
            [
                tf.keras.layers.Embedding(2, 128),
                tf.keras.layers.Dense(256, activation="tanh"),
            ]
        )

    def _load_vocab_data(self) -> Tuple[np.ndarray, np.ndarray]:
        unique_hotel_id = np.load(HOTEL_LIST_PATH, allow_pickle=True)
        unique_travel_purpose = np.load(TRAVEL_LIST_PATH, allow_pickle=True)

        return unique_hotel_id, unique_travel_purpose

    def call(self, features: Dict[str, tf.Tensor]) -> tf.Tensor:
        # Define how the ranking scores are computed:
        # Take the dot-product of the user embeddings with the movie embeddings.

        travel_embed = self.travel_embeddings(features["travel_purpose"])
        hotel_embed = self.hotel_embeddings(features["hotel_id"])
        gender_embed = self.gender_embeddings(features["gender"])
        device_embed = self.device_embeddings(features["desktop"])

        return tf.reduce_sum(
            travel_embed * gender_embed * device_embed * hotel_embed, axis=2
        )
