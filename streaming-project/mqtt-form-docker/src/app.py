#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import json
import time
import paho.mqtt.client as mqtt
from datetime import datetime
import random
client_id = ""
client = mqtt.Client(client_id=client_id)
user = ""
password = ""
client.username_pw_set(user, password)
client.connect("10.26.1.171")
topic = 'plusone'
sendStr = ""

machine_name = 'LCG-' + str(random.randint(1000,9999))
print(machine_name)
# with open('./laser-20180102.csv', 'r') as csvfile:
with open('/opt/app/laser-20180102.csv', 'r') as csvfile:
	fieldnames = ("program name","machine name","material name","work-center","order of processing", 
		"number of sheets","start time","finish time","process time","good","bad","status",
		"schedule name","saveing date/time","processing division")

	reader = csv.DictReader(csvfile, fieldnames)
	data =[]
	
	for row in reader:
		sendStr = "0x01:"+ row["program name"] + " 0x02:" + machine_name + " 0x03:" + row["material name"] +\
				" 0x04:" + row["work-center"] + " 0x05:" + row["order of processing"] + " 0x06:" + row["number of sheets"] +\
				" 0x07:" + row["start time"] + " 0x07:" + row["finish time"] + " 0x08:" + row["process time"] + " 0x09:"+ row["status"]+\
				" 0x10:" + row["schedule name"] + " 0x11:" + row["saveing date/time"] + " 0x12:" + row["processing division"]
		client.publish(topic, sendStr)
		sleepMin = row["process time"][2:4]
		sleepTime = int(sleepMin) * 60 + int(row["process time"][5:7])
		print(datetime.now().strftime("\nMQTT SENT@20%y-%d-%m %H:%M:%S") + ":\n'''''''\n" + sendStr + "\n'''''''" )
		time.sleep(sleepTime)