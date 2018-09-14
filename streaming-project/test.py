import csv
import json
import sys
import time
import paho.mqtt.client as mqtt
client_id = ""
client = mqtt.Client(client_id=client_id)
user = ""
password = ""
client.username_pw_set(user, password)
client.connect("localhost")
topic = 'plusone'

csvfile = open('./laser-20180102.csv', 'r')
fieldnames = ("program name","machine name","material name","work-center","order of processing", 
              "number of sheets","start time","finish time","process time","good","bad","status", 
              "schedule name","saveing date/time","processing division")



filename = './balanced_train_segments.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    a = list(reader)
    n = len(a)
    try:
        for row in range(2000,n):
            print(a[row])
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    
