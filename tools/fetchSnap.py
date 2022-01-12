#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import requests
import json
import time
def fetch():
    url = "https://helium-snapshots.nebra.com/latest.json"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    ret = response.text;
    return json.loads(ret)['height'];

def writefile():
    filename = '/www/wwwroot/pisces-firmware.sidcloud.cn/firmware-update/tools/snap-nebra.sh'
    with open(filename, 'w') as file_object:
        file_object.write("#!/bin/bash \n")
        file_object.write("sudo wget https://helium-snapshots.nebra.com/snap-"+str(fetch())+" -O /home/pi/hnt/miner/snap/latest\n")
        file_object.write("sudo docker exec miner miner snapshot load /var/data/snap/latest")
    loop();

def loop():
    time.sleep(1800);
    print("another round");
    init();

def init():
    print("begian");
    writefile();

init();