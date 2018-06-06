# MQTT from Docker 

本文件介紹如何將MQTT發送端用Docker Container實現，取代將MQTT發送建立在樹莓派上。
提醒：
* 不會特別提及dockerfile撰寫的語法細節，需要可查看docker官方文件。
* 不會特別說明MQTT概念。


## Dockerfile 
Dockerfile是一個腳本，包含兩個部分：
* 指令(Instrunction)
* 要做的行為(Argument)
* `#`為註解
```dockerfile=
# Comment
INSTRUCTION Arguments
```

* 建構Image的時候我們會指定路徑，`docker build`的指令會將<路徑>下的所有內容打包，所以建構dockerfile的時候請另外開一個新的資料夾，不然到時候東西都被包起來了！

* Image是多層存儲每一層是在前一層的基礎上進行的修改，容器也是多層存儲是在以鏡像為基礎層在其基礎上加一層作為容器運行時的儲存層，產生這些快取image之後，假設我們有重複的步驟像(RUN apt-get updeat 這種常會用到的)我們在往後build dockerfile的時候就不用又重跑一次。

## MQTT from docker實作：
介紹完了dockerfile如何操作後，就開始實作dockerfile吧！

* 建立一個資料夾，裡面會包含檔名為`dockerfile`以及一個`src`資料夾。
* `src`資料夾內包含Python用來發送MQTT的程式碼，與其他需要的文件（例如我的Python檔會讀取csv）。
* `requirement.txt` 記得也要放入`src`。

### 資料夾內結構：
```
.
├── dockerfile
└── src
    ├── app.py
    ├── csv_file.csv
    └── requirement.txt
```
### requirement.txt 內容：
因為本次範例只會用到`paho-mqtt`這個套件，所以只需要：
```
paho-mqtt
```
### app.py 內容：
* 記得檔名要叫做`app.py`，這樣丟到容器內才找的到，至於想發送什麼內容就依照個人需求撰寫了。
```python=
# -*- coding: utf-8 -*-
import csv
import json
import time
import paho.mqtt.client as mqtt
import sys
from datetime import datetime 
client_id = ""
client = mqtt.Client(client_id=client_id)
user = ""
password = ""
client.username_pw_set(user, password)
client.connect("your_Ip")
topic = 'your_topic'
sendStr = ""

with open('/opt/app/your_csv_file.csv', 'r') as csvfile:
	
    (依照個人想發送格式設定改寫)

client.publish(topic, sendStr)
print(datetime.now().strftime("\nMQTT SENT@20%y-%d-%m %H:%M:%S") + ":\n'''''''\n" + sendStr + "\n'''''''" )
time.sleep(3)
```
### Dockerfile 內容：
* `From` :基底映像檔選擇`ubuntu`版本為`14.04`
* `MAINTAINER` : 維護者。
* `3-8` : 安裝`python`環境。
* `9-10` : 安裝`mosquitto`和`mosquitto-clients`，因為我們需要發送`MQTT`，需要安裝`broker`。
* `COPY` : 複製本地的檔案到容器內。在前面我先mkdir建立資料夾，接著把`src`資料夾複製到`/opt/app`內。
* `13`：安裝`requirement`的Python套件。
* `14`：增加兩個可用參數`python3`, `app.py`。
```dockerfile=
FROM ubuntu:14.04
MAINTAINER plusoneeeLiao
RUN apt-get update -y \
	&& apt-get install -y \
	      python3 -y
RUN apt-get update -y \
	&& apt-get install python3-pip  -y \
 	&& apt-get autoclean 
RUN apt-get install mosquitto mosquitto-clients -y 
RUN mosquitto -d 
RUN mkdir opt/app
COPY ./src ./opt/app
RUN cd opt/app && pip3 install -r requirement.txt 
CMD ["python3","app.py"]
```

### Build Dockerfile:
執行指令
* `-t` : 後面為image名稱。
```shell=
docker build . -t mqtt-streaming
```
```
Sending build context to Docker daemon  2.555MB
Step 1/10 : FROM ubuntu:14.04
 ---> 8cef1fa16c77
Step 2/10 : MAINTAINER plusoneeeLiao
 ---> Using cache
 ---> b307afc227a4
Step 3/10 : RUN apt-get update -y 	&& apt-get install -y 	      python3 -y
 ---> Using cache
 ---> 9e2ba0125874
Step 4/10 : RUN apt-get update -y 	&& apt-get install python3-pip  -y  	&& apt-get autoclean
 ---> Using cache
 ---> 106364f69e3d
Step 5/10 : RUN apt-get install mosquitto mosquitto-clients -y
 ---> Using cache
 ---> 33bb1e8119ff
Step 6/10 : RUN mosquitto -d
 ---> Using cache
 ---> 68a61723e57b
Step 7/10 : RUN mkdir opt/app
 ---> Using cache
 ---> 1c644a2332df
Step 8/10 : COPY ./src ./opt/app
 ---> Using cache
 ---> c3c299b0473b
Step 9/10 : RUN cd opt/app && pip3 install -r requirement.txt
 ---> Using cache
 ---> 0250e0e1129c
Step 10/10 : CMD ["python3","/opt/app/app.py"]
 ---> Using cache
 ---> cd8488df6d0f
Successfully built cd8488df6d0f
Successfully tagged mqtt-streaming:latest
```
成功了！接下來就可以看是否有成功產生Image，指令：
```shell
docker images
```
會看到多了一個`mqtt-streaming`的映像檔：
```
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
mqtt-streaming        latest              cd8488df6d0f        11 minutes ago      437MB
```
最後，執行一個容器！
```shell
docker run -tid mqtt-streaming  python3 /opt/app/app.py
```
接下來檢視容器是否活著：
```
docker ps
```
看到以下畫面，docker還活著就幾乎成功了！
```
CONTAINER ID        IMAGE               COMMAND                  CREATED                  STATUS              PORTS               NAMES
18a4532838d8        mqtt-streaming      "python3 /opt/app/ap…"   Less than a second ago   Up 1 second                             tender_cray
```
那開啟spark來試試看是否有接收到MQTT發送的資料吧！
* `my_topic` : MQTT主題。 
```
spark-submit --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0 stream-mqtt-example.py localhost:1883 my_topic
```

如圖：
在python程式碼中，我設定每3秒發送一次mqtt訊息，可以看到在spark streaming的主機上接收到訊息並列印出來。

![Imgur](https://i.imgur.com/qvIg4LK.png)

接下來多開幾個容器發送MQTT試試看吧！
如下圖，我總共開了6個docker container發送訊息：
![Imgur](https://i.imgur.com/txE7Fuk.png)

最後，查看`Spark Streaming`是否能成功接收到。
如圖，可以看到接收到的訊息變頻繁了：
![Imgur](https://i.imgur.com/lIbDFQS.png)
