# Apache Kafka

![Imgur](https://i.imgur.com/GbCcMOe.png)
如上圖，一個`Kafka`群集包含多個`Producer`、`broker`、`Consumer Group`及一個`zookeeper`集群。`Producer`透過`push`將消息發佈到`broker`，`Consumer`透過`pull`方式從`broker`訂閱並消費訊息。
* `Broker`: Kafka集群包含一個或多個服務器，這種服務器被稱為broker，支持水平擴展，`broker`數量越多集群數據處理能力越高。
* `Topic`: 每條發佈到Kafka集群的消息都有一個類別，這個類別被稱為Topic。（物理上不同Topic的消息分開存儲，邏輯上一個Topic的消息雖然保存於一個或多個broker上但用戶只需指定訊息的Topic就可生產或消費數據，不需要關心數據存於何處）
* `Partition`: 每個Topic包含一個或多個Partition。
* `Producer`: 負責發布消息到Kafka broker。
* `Consumer`: 訊息消費者，向Kafka broker讀取消息的客戶端。
* `Consumer Group`:每個Consumer屬於一個特定的Consumer Group（可為每個Consumer指定group name，若不指定group name則屬於默認的group）。

`Topic`可以當作是一個`queue`，每條訊息都要指定一個`Topic`（可理解為將消息放到哪個queue裡），`Kafka`在接收到`producer`發送的訊息後會根據均衡策略將訊息存到不同的`partition`中。為了使`Kafka`的數據處理能力可以提高，`Topic`分成一個或多個`partition`，但`partitons`數量越多，需要的資源也越多，容易導致更高的不可用性。
![Imgur](https://i.imgur.com/YB3lZpI.png)
* 每條訊息都會被加到到對應的`Partition`中，訊息以順序儲存，最晚接收的訊息最後被消費。
* 傳統的message queue會刪除已被消費的訊息，`Kafka`則會保留所有的消息，但`Kafka`也有提供兩種方式刪除舊數據：
    * 基於時間
    * 基於`Partition`文件大小
* 透過修改`/config/server.properties`，讓`Kafka`刪除前一週的數據，或在`partition`文件超過1GB時刪除舊數據，不過因為`Kafka`讀取訊息時間與文件大小無關，所以刪除過期文件並不會提高`Kafka`性能。
```
# The maximum size of a log segment file. When this size is reached a new log segment will be created.
log.segment.bytes=1073741824

# The interval at which log segments are checked to see if they can be deleted according
# to the retention policies
log.retention.check.interval.ms=300000
```
* `kafka`有了`Partition`機制後，不同的訊息可以並行寫入不同`broker`的不同`Partition`裡，在`/config/server.properties`中通過配置項`num.partitions`來指定新建`Topic`默認`Partition`數量。
```
# The default number of log partitions per topic. More partitions allow greater
# parallelism for consumption, but this will also result in more files across
# the brokers.
num.partitions=1
```
* 同一個`Topci`的一條訊息只能被同一個`Consumer Group`中的一個`Consumer`消費，但多個`Consumer Group`可同時消費這一條訊息。
* 如果需要實現廣播（發給全部或某一個`Consumer`），只需要每個`Consumer`有獨立的`Group`就可以。
* `Consumer Group`可以將Consumer進行自由的分組，不需要多次發送消息到不同`Topic`。
![Imgur](https://i.imgur.com/ewfpqKm.png)
## Install Kafka @Ubuntu 
```shell=
sudo apt-get update -y
sudo apt-get upgrade -y
```
### Installing Java
```shell=
sudo add-apt-repository -y ppa:webupd8team/java
```
會看到以下輸出：
```
gpg: keyring `/tmp/tmpkjrm4mnm/secring.gpg' created
gpg: keyring `/tmp/tmpkjrm4mnm/pubring.gpg' created
gpg: requesting key EEA14886 from hkp server keyserver.ubuntu.com
gpg: /tmp/tmpkjrm4mnm/trustdb.gpg: trustdb created
gpg: key EEA14886: public key "Launchpad VLC" imported
gpg: no ultimately trusted keys found
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
OK
```
接下來，更新ubuntu repository的metadata：
```shell=
sudo apt-get update
```
更新完之後，安裝Java8：
```shell=
sudo apt-get install oracle-java8-installer -y
```
可以查看Java版本確認是否有安裝成功：
```shell=
sudo java -version
```
如果安裝完成，你會看到以下輸出：
```shell
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)
```
### Install ZooKeeper
在安裝Apache kafka之前，需要用到`zookeeper`能夠執行，`zookeeper`是一個開源的服務，用來維持資訊組態，提供分散式同步，提供命名以及群組服務。

```shell=
sudo apt-get install zookeeperd
```
安裝完成後，它會自動執行在`port 2181`，要確認是否執行：
```shell=
netstat -ant | grep :2181
```
如果一切就緒，將會看到：
```shell
tcp6       0      0 :::2181                 :::*                    LISTEN
```
或是你也可以使用其他指令：
```shell=
service zookeeper # {start|stop|status|restart|force-reload}
```
### Install and Start Kafka Server
現在我們要開始安裝`Kafka Server`先下載`Kafka`:
```shell
wget https://archive.apache.org/dist/kafka/0.10.0.1/kafka_2.10-0.10.0.1.tgz
```
建立一個資料夾在`opt`目錄，並執行解壓縮：
```shell=
sudo mkdir /opt/Kafka
sudo tar -xvf kafka_2.10-0.10.0.1.tgz -C /opt/Kafka/
```
下一步，要開啟`Kafka server`的服務，執行位於`/opt/Kafka/kafka_2.10-0.10.0.1/bin/`的`kafka-server-start.sh`，只要執行指令：

```shell=
sudo  /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-server-start.sh /opt/Kafka/kafka_2.10-0.10.0.1/config/server.properties
```
如果成功，會看到：
```
[2018-05-14 11:38:36,279] WARN No meta.properties file under dir /tmp/kafka-logs/meta.properties (kafka.server.BrokerMetadataCheckpoint)
[2018-05-14 11:38:36,516] INFO Kafka version : 0.10.0.1 (org.apache.kafka.common.utils.AppInfoParser)
[2018-05-14 11:38:36,525] INFO Kafka commitId : a7a17cdec9eaa6c5 (org.apache.kafka.common.utils.AppInfoParser)
[2018-05-14 11:38:36,527] INFO [Kafka Server 0], started (kafka.server.KafkaServer)
[2018-05-14 11:38:36,555] INFO New leader is 0 (kafka.server.ZookeeperLeaderElector$LeaderChangeListener)
```
或是使用`nohup`在背景執行：
```shell
sudo nohup /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-server-start.sh /opt/Kafka/kafka_2.10-0.10.0.1/config/server.properties /tmp/kafka.log 2>&1 &
```
Kafka server running and listening on port 9092.

### Testing Kafka Server
為了測試伺服器是否運行，我們建立一個`Topic`叫做`testing`：
```shell
sudo /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing
```
接著，就可以看到輸出：
```
Created topic "testing".
```
現在要求`Zookeeper`列出所有`Kafka server`上可用的`Topic`：
```shell
sudo /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-topics.sh --list --zookeeper localhost:2181
```
可以看到輸出顯示：
```
testing
```
現在發佈一個簡單的訊息到主題`testing`：
```shell
sudo /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testing
```
可以開始輸入想要發送的訊息了，我們先執行監聽`testing`：
```shell
sudo /opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic testing --from-beginning
```
最後在發送端輸入一些文字吧！
例如`hello world!`，就可以看到監聽端顯示輸出：
```
hello world!
```
* 更改刪除設定
    * 在`/config/server.properties`新增
`delete.topic.enable`
* 刪除指令
```shell
/opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic testing
```
* 復原刪除資料：
```
/opt/Kafka/kafka_2.10-0.10.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 \
    --replication-factor 1 --partitions 1 --topic testing
```

## Kafka Python
```python=
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
my_topic = 'testing'

# Asynchronous by default
future = producer.send(my_topic, b'testing_')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass
# Successful result returns assigned partition and offset
print ('record_metadata.topic:',record_metadata.topic)
print ('record_metadata.partition:',record_metadata.partition)
print ('record_metadata.offset:',record_metadata.offset)
# produce json messages
mydictionary = "{'this_isKey':'value'}"
producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
#producer.send(my_topic, {'hello': 'world'})
producer.send(my_topic, mydictionary)
def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception
# block until all async messages are sent
producer.flush()
# configure multiple retries
producer = KafkaProducer(retries=5)
                                   
```


