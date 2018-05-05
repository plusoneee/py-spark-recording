#!/usr/bin/python3


import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
from elasticsearch import Elasticsearch
from datetime import datetime

def send_streaming_to_Elastic(data):
    global id_num
    es = Elasticsearch()
    doc = data
    stat_es = es.index(index="customer", doc_type="mytype", body=doc, id=datetime.now().strftime("%Y%m%d%H%M%S") )
    if(stat_es['created']):print('Insert data ok!')    


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: mqtt_wordcount.py <broker url> <topic>"
        exit(-1)
    sc = SparkContext(appName="PythonStreamingMQTT_ELK")
    ssc = StreamingContext(sc, 1) 
    brokerUrl ='tcp://'+sys.argv[1]
    topic = sys.argv[2]
    lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    mqtt_get_str = lines.map(lambda word:'{"'+topic+'"'+":"+'"'+word+'"}')
    #mqtt_get_str.pprint()
    mqtt_get_str.foreachRDD(lambda rdd: rdd.foreach(send_streaming_to_Elastic))
    ssc.start()
    ssc.awaitTermination()

