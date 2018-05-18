
import json
from kafka import KafkaConsumer

my_topic = 'testing'
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(my_topic,
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("topic: %s, partition:%d, offset:%d, : key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8')))

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)




# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)
# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
'''
consumer2 = KafkaConsumer(my_topic,
                          group_id='my-group',
bootstrap_servers='localhost:9092')
'''
