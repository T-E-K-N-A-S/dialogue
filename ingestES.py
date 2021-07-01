from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, parallel_bulk
from dataloader import SRT
import config
data = SRT("data/S04E01.srt",series="Community",season=4,episode=1)

elastic_client = Elasticsearch(config.ELASTIC_SERVER_URL)
elastic_client.indices.create(index=config.ELASTIC_INDEX, include_type_name = True)


