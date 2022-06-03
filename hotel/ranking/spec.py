from typing import List, Optional
from pydantic import BaseModel


class GetRankingSpec(BaseModel):
    hotel_ids: List[int]
    device: bool
    travel_purpose: Optional[str] = None
    gender: Optional[int] = None


class GetRankingResult(BaseModel):
    hotel_ids: List[int]
