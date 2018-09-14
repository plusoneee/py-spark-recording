import json
from elasticsearch import Elasticsearch
def send_streaming_to_Elastic(data):
    es = Elasticsearch()
    doc = data
    print(doc)
    stat_es = es.index(index="index_name", doc_type="test-type", body=doc)

for line in open('powerMeter.json', 'r'):
    line = json.loads(line)
    data = {}
    data['Humidity'] = line['Humidity']
    data['Temperature'] = line['Temperature']
    data['currents'] = line['currents']
    data['timestamp'] = line['time']['$date']
    send_streaming_to_Elastic(data)
