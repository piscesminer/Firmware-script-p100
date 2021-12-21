# coding:utf-8
import os
import router
import json
import api
import getTest
import getIp
import getCpu
import getMiner
import info
import datetime

def infoCollection():
    timenow = timeCollection();
    gpsStatus = 1;
    rawInfo = info.getInfo();
    newInfo =  json.loads(rawInfo)
    rawIp = getIp.networkInfo("eth0")
    newIp = json.loads(rawIp)
    rawPublicIp = json.loads(getTest.getPublicIp())
    rawMinerHeight = json.loads(getMiner.info_height());
    rawVersion = json.loads(getVersion());
    version = rawVersion["version"];
    try:
        version = rawVersion["version"];
    except:
        version = "error";
    try:
        DiskUsed = newInfo["DiskUsed"];
    except:
        DiskUsed = "error";

    try:
        DiskTotal = newInfo["DiskTotal"];
    except:
        DiskTotal = "error";
    try:
        RamFree = newInfo["RamFree"];
    except:
        RamFree = "error";
    try:
        CpuTemp = newInfo["CpuTemp"];
    except:
        CpuTemp = "error";
    try:
        RamUsed = newInfo["RamUsed"];
    except:
        RamUsed = "error";
    try:
        DiskPerc = newInfo["DiskPerc"];
    except:
        DiskPerc = "error";
    try:
        RamTotal = newInfo["RamTotal"];
    except:
        RamTotal = "error";
    try:
        CpuUsage = newInfo["CpuUsage"];
    except:
        CpuUsage = "error";
    try:
        insideIp = newIp["IpAddress"]
    except:
        insideIp = "error";
    try:
        Ble = getTest.testBle();
    except:
        Ble = "error";
    try:
        PublicIp = rawPublicIp["PublicIp"];
    except:
        PublicIp = "error";
    try:
        BlockAge = rawMinerHeight["BlockAge"]
    except:
        BlockAge = "error";
    try:
        SyncHeight = rawMinerHeight["SyncHeight"]
    except:
        SyncHeight= "error";

    ret=[{"code":"S0401001","val":timenow},{"code":"S0401002","val":gpsStatus},{"code":"S0401003","val":CpuTemp},{"code":"S0401004","val":insideIp},{"code":"S0401005","val":CpuUsage},{"code":"S0401006","val":DiskTotal},{"code":"S0401007","val":DiskUsed},{"code":"S0401008","val":RamTotal},{"code":"S0401009","val":RamUsed},{"code":"S040100A","val":version},{"code":"S040100B","val":BlockAge},{"code":"S040100C","val":SyncHeight},{"code":"S040100D","val":Ble},{"code":"S040100E","val":"21.0"},{"code":"S040100F","val":"21.0"},{"code":"S0401010","val":PublicIp}]
    return json.dumps(ret)

def timeCollection():
     return str(datetime.datetime.now())

def gpsData():
    ret = getTest.shell("bash /home/pi/api/tool/getGps.sh")
    return ret;

def getVersion():
    f = open('/home/pi/api/tool/version', 'r')
    version = f.read()
    return version;