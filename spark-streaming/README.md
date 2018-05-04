### Eample 01
```
$ nc -lk 9999
```
```
$ spark-submit streaming-example01.py <ip> 9999
```

### mqtt stream example
```
spark-submit  --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0 mqtt_streaming-example.py localhost:1883 topic
```

### insert-mqttdata-ealstic
```
spark-submit  --packages org.apache.bahir:spark-streaming-mqtt_2.11:2.0.0 insert-mqttdata-ealstic.py localhost:1883 topic
```
