import csv
import json

import time
import paho.mqtt.client as mqtt
client_id = ""
client = mqtt.Client(client_id=client_id)
user = ""
password = ""
client.username_pw_set(user, password)
client.connect("10.26.1.171")
topic = 'plusone'

csvfile = open('./laser-20180102.csv', 'r')
fieldnames = ("program name","machine name","material name","work-center","order of processing", 
              "number of sheets","start time","finish time","process time","good","bad","status", 
              "schedule name","saveing date/time","processing division")
reader = csv.DictReader(csvfile, fieldnames)
data =[]
for row in reader:
    data.append({ 
        "program_name":row["program name"],
        "machine_name":row["program name"],
        "material_name":row["material name"],
        "work_center":row["work-center"],
        "order_of_processing":row["order of processing"],
        "start_time":row["start time"],
        "finish_time":row["finish time"],
        "process_time":row["process time"],
        "good":row["good"],
        "status":row["status"],
        "schedule_name":row["schedule name"],
        "saveing_date/time":row["saveing date/time"],
        "processing_division":row["processing division"]
    })

for i in range(0,2000):
    data[i] = str(data[i])
    client.publish(topic, data[i])
    print(data[i])
    time.sleep(10)
    
