from typing import Dict
import tensorflow as tf
import tensorflow_ranking as tfr
from injector import inject

from hotel.constants import MODEL_WEIGHT_PATH
from .spec import GetRankingSpec, GetRankingResult
from .algo import HotelRankingModel


class RankingAccessor:
    @inject
    def __init__(self) -> None:
        model = HotelRankingModel()
        model.load_weights(MODEL_WEIGHT_PATH)
        self.model = model

    def generate(self, spec: GetRankingSpec) -> GetRankingResult:
        """
        Model generate ranking from
        """
        inputs = self._construct_inputs(spec)
        scores = self.model(inputs)
        hotels = tfr.utils.sort_by_scores(
            scores, [tf.expand_dims(spec.hotel_ids, axis=0)]
        )[0]
        return GetRankingResult(hotel_ids=list(hotels.numpy().tolist())[0])

    def _construct_inputs(self, spec: GetRankingSpec) -> Dict[str, tf.Tensor]:
        inputs = {
            "travel_purpose": tf.expand_dims(
                tf.repeat(spec.travel_purpose, repeats=len(spec.hotel_ids)), axis=0
            ),
            "hotel_id": tf.expand_dims(spec.hotel_ids, axis=0),
        }
        return inputs
