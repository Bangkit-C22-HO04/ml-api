import tensorflow as tf
from injector import inject

from hotel.constants import MODEL_PATH


class RankingAccessor:
    @inject
    def __init__(self) -> None:
        self._model = tf.saved_model.load(MODEL_PATH)
