from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
from dataloader import SRT
import config
import json

elastic_client = Elasticsearch(config.ELASTIC_REMOTE_SERVER_URL)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "conversation in movies, series & podcasts"}

@app.get("/dialogue")
async def root():
    JS = elastic_client.search(index = config.ELASTIC_INDEX)
    return {"message": "conversation in movies, series & podcasts","JS":JS}

