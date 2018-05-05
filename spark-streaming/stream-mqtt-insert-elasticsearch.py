#!/usr/bin/python3
import logging
logging.basicConfig(level=logging.ERROR)

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
from elasticsearch import Elasticsearch
from datetime import datetime
import json


def send_streaming_to_Elastic(data):
    es = Elasticsearch()
    doc = json.loads(data)
    stat_es = es.index(index="machan-laser", doc_type="test-type", body=doc)
    print(type(doc))
    print(doc)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: mqtt_wordcount.py <broker url> <topic>"
        exit(-1)
    sc = SparkContext(appName="PythonStreamingMQTT_ELK")
    ssc = StreamingContext(sc, 1) 
    brokerUrl ='tcp://'+sys.argv[1]
    topic = sys.argv[2]
    lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    mqtt_get_str = lines.map(lambda word:word.replace("'", "\""))
    mqtt_get_str.pprint()
    mqtt_get_str.foreachRDD(lambda rdd: rdd.foreach(send_streaming_to_Elastic))
    ssc.start()
    ssc.awaitTermination()

