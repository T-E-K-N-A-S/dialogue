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
async def dialogue():
    JS = elastic_client.search(index = config.ELASTIC_INDEX,size=100)
    return {"message": "conversation in movies, series & podcasts","data":JS["hits"]["hits"],"count":JS["hits"]["total"]["value"]}


@app.get("/indices")
async def indices():
    indices=elastic_client.indices.get_alias().keys()
    return {"message": sorted(indices)}


@app.get("/search/{text}")
async def search(text):
    print("Searching... ",text)
    JS = elastic_client.search(index = config.ELASTIC_INDEX,size=100, body={
  "query": {
    "match_phrase_prefix": {
      "txt": text
    }
  }
})
    return {"message": "conversation in movies, series & podcasts","data":JS["hits"]["hits"],"count":JS["hits"]["total"]["value"]}