from injector import Binder, Module, singleton

from .accessor import RankingAccessor
from .service import RankingService


class RankingModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(RankingAccessor, to=RankingAccessor, scope=singleton)
        binder.bind(RankingService, to=RankingService, scope=singleton)
