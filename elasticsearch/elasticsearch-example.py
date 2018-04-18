
from datetime import datetime
#connect to our cluster
from elasticsearch import Elasticsearch
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es = Elasticsearch()


doc={"any": "data", "timestamp": datetime.now()}

stat_es = es.index(index="my-index", doc_type="test-type", id=43, body=doc)
print(stat_es['created'])

stat_es = es.get(index="my-index", doc_type='test-type', id=43)
print(stat_es['_source'])




