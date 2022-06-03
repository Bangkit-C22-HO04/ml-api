from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .di import injector
from hotel.ranking.service import RankingService
from hotel.ranking.spec import GetRankingSpec, GetRankingResult

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

ranking_service = injector.get(RankingService)


@app.on_event("startup")
def startup():
    injector.get(RankingService)


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/generate", response_model=GetRankingResult)
def generate(spec: GetRankingSpec):
    return ranking_service.generate(spec)
