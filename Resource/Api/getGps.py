import threading
from threading import Lock,Thread
import serial
from time import ctime,sleep
import json
import api
import router
import pynmea2
time = 0; 


def reader():
    ret = [];
    ser = serial.Serial("/dev/serial0",9600)
    i=10
    while i>0:
        i=i-1;
        line = str(str(ser.readline())[2:])
        ret.append(line)
    if(len(ret)>5):
        return json.dumps(ret);
    else:
        return router.server_error();
    

def decode():

    ser = serial.Serial("/dev/serial0",9600)
    while True:
        line = ser.readline()
        if line.startswith('$GNRMC'):
            rmc = pynmea2.parse(line)
            print (line);
            # print "Latitude:  ", float(rmc.lat)/100
            # print "Longitude: ", float(rmc.lon)/100
            break 
if __name__ == '__main__':
    print(reader())
