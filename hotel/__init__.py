from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .di import injector
from hotel.ranking.service import RankingService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.on_event("startup")
async def startup():
    injector.get(RankingService)
