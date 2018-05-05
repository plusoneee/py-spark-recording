# Elasticsearch

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

#### 列出所有Index:
```sh
$ curl localhost:9200/_cat/indices?v
```

#### 列出Index下的所有資料：
```sh
curl 'localhost:9200/<index name>/_search?q=*&pretty'
```
* 回傳參數：
  * took: 在 Elasticsearch 內搜尋所花費的時間(單位: 毫秒)
  * timed_out: 這次搜尋是否有超時(需要設定超時時間)
  * _shards: 搜尋了多少個片段(成功與失敗個數)
  * hits: 搜尋結果回傳
    * hits.total: 搜尋回傳資料筆數
    * hits.max_score: 搜尋結果最高分數
* 回傳內容：
```json
{
  "took" : 958,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 0,
    "max_score" : null,
    "hits" : [ ]
  }
}
```

#### 列出Index下所有Types
```sh
$ curl -XGET 'http://localhost:9200/<my index name>/_mapping?pretty'
```

#### 依據id刪除資料
```
curl -XDELETE 'localhost:9200/<index name>/<typen name>/<id>?pretty'
```
* 成功回傳：
```json
{
  "found" : true,
  "_index" : "my-index",
  "_type" : "my-type",
  "_id" : "id",
  "_version" : 2,
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  }
}
```




## Python Elasticsearch

### 特定資料操作
* get: 取得指定index、type、id的資料
```python
es.get(index='<index name>', doc_type='<type name>', id='<id>')
```
* delete:刪除指定的index、type、id資料
```python
es.delete(index='<index name>', doc_type='<type name>', id='<id>')
```
* update:更新指定的index、type、id資料
```python
es.update(index='<index name>', doc_type='<type name>', id='<id>', body={更新內容})
```
* 範例：
```python
es.update(
  index='my-index', 
  doc_type='test-type', 
  id='43', 
  body={ 
      "doc":{ 'any':'mydate'}
       })
```

### 批量操作

#### 條件搜尋：
* `search`：查詢滿足條件的所有資料，沒有id（index,type,body可以為None）

* 搜尋`所有`資料：
```python
query = {'query': {'match_all': {}}}
es.search(index='<index name>', doc_type='<type name>', body=query)
```
* 搜尋`'any'`中是否有`'anydata'`這筆資料：
```python
query = {'query': {'term': {'any': 'anydata'}}}
es.search(index='<index name>', doc_type='<type name>', body=query)
```
* 搜尋`'age'`大於`'40'`的資料：
```python
query = {'query': {'range': {'age': {'gt': 40}}}}
```
#### 條件刪除：
* `delete_by_query`: 刪除滿足條件的資料
* 刪除`'age'`為`'32'`的資料：
```python
query = {'query': {'match': {'age': '32'}}}
es.delete_by_query(index='<index name>', body=query, doc_type='<type name>')
```
* 刪除年齡小於30的資料：
```python
query = {'query': {'range': {'age': {'lt': 30 }}}}
es.delete_by_query(index='<index name>', body=query, doc_type='<type name>')
```

### Python範例程式碼：
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



