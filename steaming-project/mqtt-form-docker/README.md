
### Build Image:
```
docker build . -t streaming-mqtt
```
```
docker run -tid streaming-mqtt python3 /opt/app/app.py
```


### Run Spark
* topic : plusone
* ip : 10.26.1.171
```
spark-submit --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0 stream-mqtt-example.py localhost:1883 plusone
```
