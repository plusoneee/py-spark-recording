import csv
import json

import time
# import paho.mqtt.client as mqtt
# client_id = ""
# client = mqtt.Client(client_id=client_id)
# user = ""
# password = ""
# client.username_pw_set(user, password)
# client.connect("10.26.1.171")
# topic = 'plusone'

csvfile = open('./laser-20180102.csv', 'r')
fieldnames = ("program name","machine name","material name","work-center","order of processing", 
              "number of sheets","start time","finish time","process time","good","bad","status", 
              "schedule name","saveing date/time","processing division")
reader = csv.DictReader(csvfile, fieldnames)
data =[]
for row in reader:
    data.append({ 
        "0x01":row["program name"],
        "0x02":row["program name"],
        "0x03":row["material name"],
        "0x04":row["work-center"],
        "0x05":row["order of processing"],
        "0x06":row["start time"],
        "0x07":row["finish time"],
        "0x08":row["process time"],
        "0x09":row["good"],
        "0x10":row["status"],
        "0x11":row["schedule name"],
        "0x12":row["saveing date/time"],
        "0x13":row["processing division"]
    })

for i in range(0,2000):
    # data[i] = str(data[i])
    # client.publish(topic, data[i])
    sendstr = "0x01:" + str(data[0]["0x01"]) + " 0x02:" + str(data[0]["0x02"]) + " 0x03:" + str(data[0]["0x04"]) + " 0x05:" + str(data[0]["0x05"]) + " 0x06:" + str(data[0]["0x06"]) + " 0x07:" + str(data[0]["0x07"]) + " 0x08:" + str(data[0]["0x08"]) + " 0x09:" + str(data[0]["0x09"]) + " 0x10:" + str(data[0]["0x10"]) + " 0x11:" + str(data[0]["0x11"]) + " 0x12:" + str(data[0]["0x12"]) 
    # print( "0x01:"+ str(data[0]["0x01"]))
    print(sendstr)
    time.sleep(10)
    
