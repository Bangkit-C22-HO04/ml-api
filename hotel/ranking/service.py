from injector import inject

from .accessor import RankingAccessor
from .spec import GetRankingSpec, GetRankingResult


class RankingService:
    @inject
    def __init__(self, accessor: RankingAccessor) -> None:
        self.accessor = accessor

    def generate(self, spec: GetRankingSpec) -> GetRankingResult:
        result = self.accessor.generate(spec)

        return result
