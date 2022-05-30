from dataclasses import dataclass
from typing import List


@dataclass
class GetRankingSpec:
    gender: int
    travel_purpose: str


@dataclass
class GetRankingResult:
    hotel_ids: List[int]
