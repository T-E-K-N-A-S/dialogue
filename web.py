from fastapi import FastAPI
from elasticsearch import Elasticsearch
from dataloader import SRT
import config
import json
elastic_client = Elasticsearch(config.ELASTIC_REMOTE_SERVER_URL)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "conversation in movies, series & podcasts"}

@app.get("/dialogue")
async def root():

    return {"message": "conversation in movies, series & podcasts"}

