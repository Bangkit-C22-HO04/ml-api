from injector import Injector

from .ranking.module import RankingModule


injector = Injector([
    RankingModule
])
