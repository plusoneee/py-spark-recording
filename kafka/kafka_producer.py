import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
my_topic = 'testing'

# Asynchronous by default
future = producer.send(my_topic,'send_start'.encode('UTF-8'))

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
