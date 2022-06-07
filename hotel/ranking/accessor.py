import tensorflow as tf
from injector import inject

from hotel.constants import MODEL_PATH
from .spec import GetRankingSpec, GetRankingResult

class RankingAccessor:
    @inject
    def __init__(self) -> None:
        self._model = tf.saved_model.load(MODEL_PATH)

    def generate(self, spec: GetRankingSpec) -> GetRankingResult:
        '''
        Model generate ranking from
        '''
        inputs = self._get_inputs(spec)
        return GetRankingResult(
            hotel_ids=spec.hotel_ids
        )

    def _get_inputs(self, spec: GetRankingSpec) -> tf.Tensor:
        return {}
