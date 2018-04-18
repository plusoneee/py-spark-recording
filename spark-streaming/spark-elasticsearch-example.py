#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pyspark import SparkContext

sc = SparkContext(appName = 'ela-test')
conf = {"es.resource":"my-index/my-type","es.node":"localhost:9200"}
rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat",\
    "org.apache.hadoop.io.NullWritable", "org.elasticsearch.hadoop.mr.LinkedMapWritable", conf=conf)
result = rdd.first()
print (result)

