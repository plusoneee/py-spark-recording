#!/usr/bin/python3


import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
from pymongo import MongoClient
from elasticsearch import Elasticsearch

def send_streaming_to_Elastic(data):
    es = Elasticsearch() 
    doc = data
    stat_es = es.index(index="customer", doc_type="mytype", body=doc, id=9)
    stat_es = es.get(index="customer", doc_type='mytype', id=9)
    print(stat_es['_source'])
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: mqtt_wordcount.py <broker url> <topic>"
        exit(-1)
    sc = SparkContext(appName="PythonStreamingMQTT_ELK")
    ssc = StreamingContext(sc, 1)
#    conf = {"es.resource":"customer/mytype","es.node":"localhost:9200"}
#    rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat",\
#    "org.apache.hadoop.io.NullWritable", "org.elasticsearch.hadoop.mr.LinkedMapWritable", conf=conf)

    brokerUrl ='tcp://'+sys.argv[1]
    topic = sys.argv[2]

    lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    mqtt_get_str = lines.map(lambda word:'{"'+topic+'"'+":"+'"'+word+'"}')
    #mqtt_get_str.pprint()
    mqtt_get_str.foreachRDD(lambda rdd: rdd.foreach(send_streaming_to_Elastic))

    ssc.start()
    ssc.awaitTermination()

