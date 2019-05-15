# Spark Streaming (Pyspark)
在本文件中是會依序介紹`Spark Streaming`、`MQTT`通訊協定、NoSQL資料庫`Elasticsearch`操作，最後結合三者（`Spark Streaming`, `MQTT`, `Elasticsearch`）實作出發佈資料透過PySpark Streaming將資料儲存到NoSQL資料庫的過程。

## Summary
* Spark Streaming Introdution
  * Discretized Streams (DStreams)
  * A Quick Example
  * Transformations on DStreams
  
* PySpark MQTT
  * Install MQTT server
  * How Spark Subscribe a MQTT Topic

* PySpark Elasticsearch
  * Testing Elasticsearch
  * Using Elasticsearch
  * Python-ES Example
  * How Insert Data to ES from Spark

* Finally Example 
  
## Spark Streaming Introdution
`Spark Streaming`是`Spark API`的一個擴充能夠即時資料串流處理，從不同來源取得資料後利用不同RDD函式轉換資料格式或計算，最後將資料儲存到資料庫等地方，方便後續做機器學習演算法等等，如下圖：

* kafka、flume、Twitter、 ZeroMQ、Kinesis發送資料
* 透過Spark將資料做儲存到HDFS、資料庫或是顯示在Dashboard

![Imgur](https://i.imgur.com/DiHHlOL.png)

Spark Streaming和spark不同的是，它提供了一種高級的抽象類別`Discretized Stream`或稱`Dstream`，它代表一個連續的資料串流。`DStream`能夠藉由不同來源取得輸入的資料。`DStream`的內部是由序列的`RDD`組成。

詳細的`RDD fuction`使用並不會在這裡做說明，可以查看官方文件。

## Discretized Streams (DStreams)
什麼是`DStreams`？是由Spark Streaming提供的基本抽象類別，表現了一個連續的資料串流，它能夠藉`transform`由從接收來源輸入資料或處理產生的資料串流。一個`DStream`表示一個一系列連續的`RDDs`，`RDD`是Spark中不可變的抽象類別，分散式數據庫。

* 在DStream中每個`RDD`中間有一定的間隔，每個`RDD`內包含了資料，如圖：
![Imgur](https://spark.apache.org/docs/2.2.0/img/streaming-dstream.png)

* 在`DStream`上應用的任何操作(translates)都會轉換為在基礎`RDD`的操作，例如[WordCount](https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html#a-quick-example)將串流每一行的字轉換的例子中，將`flatMap`的操作應用於`DStream`行中的每個`RDD`，以生成字串的`DStream`，如圖：
![](https://spark.apache.org/docs/2.2.0/img/streaming-dstream-ops.png)

這些基礎`RDD transformations`由Spark engine計算，DStream操作隱藏了大部分的細節，並為開發人員提供了更高級的API以方便使用。

## A Quick Example
在進入如何編寫Spark Streaming程式的細節前，我們來看一個簡單的例子，程式從監聽TCP Socket的資料伺服器取得文字資料，計算文字包含的單字數：

* 首先要先導入`StreamingContext`，這是所有Streaming功能的進入點。
```python=
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
```
* 使用兩個執行執行緒創建本地`(local)`的批次處理間隔為1秒(以秒為單位分割資料串)的`StreamingContext`。
```python=
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)
```
* 利用`StreamingContext`，能夠創建一個`DStream`，它代表從TCP來源（主機位址localhost，port為9999）取得的資料。
```pyhton=
lines = ssc.socketTextStream("localhost", 9999)
```
* `lines`變數是一個DStream，表示即將獲得的資料串流。這個`DStream`的每條紀錄都代表一行文字，並利用`split`來將資料做切割變成單字。
*  `flatMap`是一個一對多的DStream操作，把`DStream`的每條紀錄都生成多個新紀錄來創建成新的`DStream`。在這個例子中，每行文字都被切分成了多個單字，我們把切割出的單字串流用`words`這個`DStream`表示。
```python=
words = lines.flatMap(lambda line: line.split(" "))
```
* `words`這個`DStream`被一對一轉換操作成了一個新的`DStream`，由（word，1）對(pair)組成。接著，就可以用這個新的`DStream`計算每批次資料的單字頻率。最後，用`wordCounts.print()`印出每秒計算的單字頻率。
```python=
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint()
```
* 值得注意的是上述的程式碼`Spark Streaming`只是準備它要執行的計算，實際上並沒有真正的執行，要真正的計算必須要調用Action函數。
```python=
ssc.start()             
ssc.awaitTermination()  
```
* 如果已經將環境準備好了，開啟終端機：
```shell=
nc -lk 9999
```
* 開啟另外一個終端機執行內建的範例程式碼:
```shell=
./bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999
```

## Transformations on DStreams
和`RDDs`很類似，`transformations`允許資料從輸入`DStream`被修改。`DStream`支援很多可用的建立在一般`Spark RDD`的`transformations`，可以到Spark官方文件[Transformations on DStreams](https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html#transformations-on-dstreams)查看細節。

---
# PySpark MQTT
在介紹Spark Streaming MQTT之前，要先介紹一下什麼是MQTT:
> [MQTT](http://mqtt.org) is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

簡單來說MQTT是一種machine-to-machine（M2M）的輕量級通訊協定，透過publish/subscribe的概念可以讓各種設備互相溝通，且需要的運算與傳輸頻寬很低。
* MQTT的傳送方式是藉由MQTT broker做分發，如下圖：

![Imgur](https://i.imgur.com/QYqZekB.png)
* Sensor端接收到溫度之後，透過`Publish`將收到的資料發送，讓`Subscribe`端接收，一次可能會有好多組Publish與Subscribe，就是透過中間的broker端去根據不同的主題（Topic）做資料的派送。



## Install MQTT server

理解MQTT的概念之後就可以來實際安裝MQTT broker了，安裝一個叫做`Mosquitto`的伺服器。

* `Mac`只需要用`brew`安裝就好：
```shell=
$ brew install mosquitto
```
完成之後，打開伺服器服務：
```shell=
$ brew services start mosquitto
```
* Ubuntu
```shell=
$ sudo apt-get install mosquitto mosquitto-clients
```

好了之後來測試一下`Mosquitto`，打開兩個終端機分別輸入：
* 訂閱： `mosquitto_sub`
```shell=
$ mosquitto_sub -h localhost -t test
```
* 發送： `mosquitto_pub`
```shell=
$ mosquitto_pub -h localhost -t test -m "Hello world!"
```
發送之後就可以看到訂閱端的終端機收到`Hello world!`了
* `-h`: host 沒有特別打的話預設是`localhost`。
* `-t`: Topic 主題，訂閱跟發送端需要同一個主題，上面我們設定的主題都是`test`。
* `-m`: 發送端多了`-m`，後面打上要發送的內容。



## How Spark Subscribe a MQTT Topic
知道MQTT的操作之後，接下來要將兩者做串接講解`Spark Streaming`訂閱接收`MQTT broker`發佈的資料。
* 和前面的介紹一樣，我們需要引入些需要用到的函式庫(包含`SparkContext`,`mqtt`等等)：
```pyhton=
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
```
* 前面引入`sys`用來接收系統的參數，下面程式碼中，我們判斷是否接收剛好三個參數分別為`pyspark.py`, `<broker url>`, `<MQTT Topic>`
```python=
if len(sys.argv) != 3:
    print >> sys.stderr, "Usage: pyspark.py <broker url> <topic>"
    exit(-1)
brokerUrl ='tcp://'+sys.argv[1]
topic = sys.argv[2]
```
* 關於`SparkContext`前面介紹過的功能這裡就不多作介紹了。
```python=
sc = SparkContext(appName="PythonStreamingMQTT")
    ssc = StreamingContext(sc, 1)
```
* 定義`lines`為`MQTT`接收到資料後創建的RDD，參數包含`StreamingContext`, `brokerUrl`, `Mqtt topic`。
```python=
lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    mqtt_get_str = lines.map(lambda word:'get world from topic'+topic+" : "+word)
    mqtt_get_str.pprint()
```
* 最後開啟執行：
```python=
ssc.start()
ssc.awaitTermination()
```    
* 好了之後就可以執行程式碼了：
```shell=
spark-submit --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0  PythonStreamingMQTT.py localhost:1883 mytopic
```
* 開啟另外一個終端機：
```shell=
mosquitto_pub -t mytopic -m hello_spark -h localhost
```
* 就能看到如下圖的結果，我們收到了`hello_spark`。當然你可以一直發佈訊息，Spark將會一直接收。

![Imgur](https://i.imgur.com/pPmpqmQ.png)

* 當然你可以持續發佈訊息，會看到Spark的終端機一直顯示資料。

# PySpark Elasticsearch

當`Spark Streaming`接收到`MQTT`發布的資料後，需要把資料給儲存起來，這時候就可以使用`ElasticSearch` (簡稱 `ES`) ，`ES`是一個`分散式搜尋引擎`，也是`NoSQL` 資料庫的一種，所有的資料都是以 `JSON` 的方式進行存取設定。用起來像是`MongoDB`，最大的不同是所有欄位都可以建立索引進行全文搜尋，而目前來說`MongoDB`只有對部分語言支援全文搜尋。


![Imgur](https://i.imgur.com/w2qkqtG.png)

* 在這不會講解`Elasticsearch`的安裝，以下解說接預設為已經安裝好環境了，也就是`Elasticsearch`已經在`9200`port運行了。
  
## Testing Elasticsearch
* 要測試ES有沒有安裝完成可以使用簡單的`GET request`：
```shell=
curl -X GET 'http://localhost:9200'
```
* 你會看到類似這樣的response：
```json=
{
  "name" : "Frankie Raye",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "2.4.6",
    "build_hash" : "5376dca9f70f3abef96a77f4bb22720ace8240fd",
    "build_timestamp" : "2017-07-18T12:17:44Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.4"
  },
  "tagline" : "You Know, for Search"
}
```
## Using Elasticsearch
* 建立Index：
```shell=
$ curl -XPUT localhost:9200/<index name>?pretty
```
* 成功:
```json=
{
  "acknowledged" : true
}
```
* 失敗（已存在）:
```json=
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
* 刪除`Index`：
```shell=
curl -XDELETE localhost:9200/<index name>?pretty
```
* 成功回傳：
```json=
{
  "acknowledged" : true
}
```

* 列出所有`Index`：
```shell=
curl localhost:9200/_cat/indices?v
```

* 列出`Index`下的所有資料：
```shell=
curl 'localhost:9200/<index name>/_search?q=*&pretty'
```
* 回傳參數：
  * `took`: 在 Elasticsearch 內搜尋所花費的時間(單位: 毫秒)
  * `timed_out`: 這次搜尋是否有超時(需要設定超時時間)
  * `_shards`: 搜尋了多少個片段(成功與失敗個數)
  * `hits`: 搜尋結果回傳
    * `hits.total`: 搜尋回傳資料筆數
    * `hits.max_score`: 搜尋結果最高分數
* 回傳內容：
```json=
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
* 列出`Index`下所有`Types`
```shell=
curl -XGET 'http://localhost:9200/<my index name>/_mapping?pretty'
```

* 依據`id`刪除資料
```shell=
curl -XDELETE 'localhost:9200/<index name>/<typen name>/<id>?pretty'
```
以上就是基本的`Elasticsearch`操作，為了要在`Spark`中操作`ES`，必須理解怎麼透過`Python`進行操作。

## Python-Elasticsearch
知道`ES`的基本操作後，接下來會簡單介紹用Python操作Elasticsearch API，如果要知道更詳細的內容可以到直接到[Elasticsearch API Documentation](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch)

* 一開始我們必須引入`elasticsearch`到程式碼中：
```python=
from elasticsearch import Elasticsearch
es = Elasticsearch()
```
* 若在之前沒有創建`Index`透過Python程式碼：
```python=
# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='my-index', ignore=400)
```
* `get`：取得指定index、type、id的資料
```python=
es.get(index='<index name>', doc_type='<type name>', id='<id>')
```
* `delete`：刪除指定的index、type、id資料
```python=
es.delete(index='<index name>', doc_type='<type name>', id='<id>')
```
* `update`：更新指定的index、type、id資料
```python=
es.update(index='<index name>', doc_type='<type name>', id='<id>', body={更新內容})
```
* Update範例：
```python=
es.update(
  index='my-index', 
  doc_type='test-type', 
  id='43', 
  body={"doc":{ 'any':'mydate'}})
```

### Python-ES Example：
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
stat_es = es.get(index="my-index", doc_type='my-type', id=1)
print(stat_es['_source'])
```

## How Insert Data to ES from Spark
`Spark Streaming`、`MQTT`、`Elasticsearch`都理解後，我們就可以結合三者，`Streaming`不斷接收`MQTT`資料後存到`ES`資料庫內，直接來看看程式碼吧！

* 一開始當然要引入需要的函式庫，包含`sys`, `json`, `elasticsearch` 和最重要的`StreamingContext`，而`datetime`是為了紀錄每筆資料接收的時間。
```python=
#!/usr/bin/python3
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
from elasticsearch import Elasticsearch
from datetime import datetime
import json
```
* 這裡的程式碼在之前有說明過，接收終端傳入的變數分別設定為`Python file`, `broker url`, `Topic`。
* 透過`map` 或其他`RDD function`更改資料格式（依照你需要的資料格式操作），這邊我僅僅使用`replace()`更換字元而已。
```python=
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: mqtt_streaming.py <broker url> <topic>"
        exit(-1)

    sc = SparkContext(appName="PythonStreamingMQTT_ELK")
    ssc = StreamingContext(sc, 1)

    brokerUrl ='tcp://'+sys.argv[1]
    topic = sys.argv[2]
    lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    mqtt_get_str = lines.map(lambda word:word.replace("'", "\""))
    mqtt_get_str.pprint()                         
```
* 因為透過`Streaming`，不會只收有一筆(RDD)資料，而是在一段時間內收到一批(RDD)的資料，因此我們需要進一步循環處理每一個`RDD`，類似用`For`迴圈但`RDD`則是使用`foreachRDD()`來處理每一筆串流收到的資料。
```python=
    mqtt_get_str.foreachRDD(lambda rdd: rdd.foreach(send_streaming_to_Elastic))
```
* 前面提過要真正開始執行必須要有`Action`，這裡使用`start()`：
```python=
    ssc.start()
    ssc.awaitTermination() 
```
* 前面的`foreachRDD()`內，我們放入了一個`send_streaming_to_Elastic`，在每時間間隔接收到的一批`RDD`都會執行此方法，方法內我們執行將`data`（也就是收到的資料）轉成`Json`格式，接著將資料存入`Elasticsearch`。
```python=
def send_streaming_to_Elastic(data):
    es = Elasticsearch()
    doc = json.loads(data)
    stat_es = es.index(index="machan-laser", doc_type="test-type", body=doc)
    print('data insert to Elasticsearch at'+ datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
```
# Finally Example
最後，我們要來測試程式碼是否成功

* 先執行`Spark`：
```shell=
spark-submit  --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0 stream-mqtt-example.py localhost:1883 plusone
```

* MQTT發送測試訊息：
```shell=
mosquitto_pub -t plusone -h 10.26.1.171 -m 
"{'program_name': 'plusone-test-sparkstreaming',
'machine_name': 'test-machine-plusone',
'material_name': 'A5052H-1.5',
'work_center': '0', 
'order_of_processing': '1', 
'start_time': '2017/02/10 16:42:23', 'finish_time': '2017/02/10 16:45:46', 'process_time': '0:03:23', 
'good': '1', 'status': '0', 
'schedule_name': '', 
'saveing_date/time': 
'2017/02/10 16:42:23', 
'processing_division': '4199170'}"
```
* 如果成功的話，就會看到程式碼中`print()`內的`data insert to Elasticsearch at 目前的時間`在終端機，如圖： 

![Imgur](https://i.imgur.com/aVD4Vny.png)

* 若`Elasticsearch`有裝plugin可以查看資料內容的話，也可以查看，如圖，可以看到`ES`內新增了一筆資料，內容和`MQTT`發佈的內容是一樣的：
 
![Imgur](https://i.imgur.com/i1CwHKY.png)
