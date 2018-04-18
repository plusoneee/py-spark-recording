# Elasticsearch

#### 列出所有Index:
```sh
$ curl localhost:9200/_cat/indices?v
```
#### 列出Index下所有Types
```sh
$ curl -XGET 'http://localhost:9200/<my index name>/_mapping?pretty'
```
#### 建立Index
```sh
$ curl -XPUT localhost:9200/<index name>?pretty
```
* 成功回傳:
```json
{
  "acknowledged" : true
}
```
* 失敗（已存在）:
```json
{
  "error" : {
    "root_cause" : [ {
      "type" : "index_already_exists_exception",
      "reason" : "already exists",
      "index" : "test-index"
    } ],
    "type" : "index_already_exists_exception",
    "reason" : "already exists",
    "index" : "test-index"
  },
  "status" : 400
}
```
#### 刪除Index
```sh
curl -XDELETE localhost:9200/<index name>?pretty
```
* 成功回傳:
```json
{
  "acknowledged" : true
}
```

## python api
```python
from datetime import datetime
#connect to our cluster
from elasticsearch import Elasticsearch
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# default :'host': 'localhost', 'port': 9200}
es = Elasticsearch() 

doc={"any": "data", "timestamp": datetime.now()}
stat_es = es.index(index="my-index", doc_type="test-type", id=1, body=doc)
print(stat_es['created'])

stat_es = es.get(index="my-index", doc_type='test-type', id=1)
print(stat_es['_source'])
```

