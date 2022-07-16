from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, parallel_bulk
from dataloader import SRT
import config
import json
data = SRT("data/S04E01.srt",series="Community",season=4,episode=1)

elastic_client = Elasticsearch(config.ELASTIC_REMOTE_SERVER_URL)

# elastic_client.indices.delete(index=config.ELASTIC_INDEX, request_timeout=30)
elastic_client.indices.create(index=config.ELASTIC_INDEX, include_type_name = True, request_timeout=30)


mapping = elastic_client.indices.get_mapping(index = config.ELASTIC_INDEX, request_timeout=30)
print(mapping)


js = []
for obj in data.parsed_data:
    action = {
                "index": {
                        "_index": config.ELASTIC_INDEX,
                    }
            }
    js.append(action)
    dic = obj.__dict__
    dic["movie"] = data.movie
    dic["series"] = data.series
    dic["season"] = data.season
    dic["episode"] = data.episode
    js.append(obj.__dict__)


print(js)
push = elastic_client.bulk(body = js,index = config.ELASTIC_INDEX, request_timeout=300)
count = elastic_client.search(index = config.ELASTIC_INDEX, request_timeout=30)
print(push,count)
