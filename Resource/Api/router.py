# coding:utf-8

import os
import sys
import json
import socket
import api
import info
import getIp
import getCpu
import getMiner
import getTest
import getGps
import getKafka
import time
import actionBasic

'''
🍺路由系统，根据路由系统进行跳转
'''
def router(client,method,path,parame):
    if(path == "/"):
        api.responsing(client,index());
    elif(path == "/api"):
        api.responsing(client,index());
        ##🍺设备硬件信息
    elif(path == "/api/hotspot/info"):
        api.responsing(client,hotspot_info());
    elif(path == "/api/hotspot/eth0"):
        api.responsing(client,hotspot_eth0());
    elif(path == "/api/hotspot/wlan0"):
        api.responsing(client,hotspot_wlan0());
    elif(path == "/api/hotspot/cpuinfo"):
        api.responsing(client,hotspot_cpuinfo());
        ##🍺设备Miner信息
    elif(path == "/api/miner/keys"):
        api.responsing(client,miner_keys());
    elif(path == "/api/miner/sync"):
        api.responsing(client,getMiner.info_height());
        ##🍺测试相关debug接口
    # elif(path == "/api/test/shell"):
    #     api.responsing(client,getTest.shell(parame[0][1]));
    elif(path == "/api/test/ble"):
        api.responsing(client,getTest.testBle());
    elif(path == "/api/test/gps"):
        api.responsing(client,getGps.reader());
    elif(path == "/api/test/ecc"):
        api.responsing(client,getTest.testEcc());
    elif(path == "/api/test/ecc/provision"):
        api.responsing(client,getTest.provisionEcc());
    elif(path == "/api/test/ecc/onboarding"):
        api.responsing(client,getTest.onboardingEcc());
    elif(path == "/api/test/ecc/provisionOnboard"):
        api.responsing(client,provision_onboard());
    elif(path == "/api/test/minerSn/init"):
        api.responsing(client,getTest.e2init());
    elif(path == "/api/test/minerSn/read"):
        api.responsing(client,getTest.e2read());
    elif(path == "/api/test/minerSn/write"):
        api.responsing(client,getTest.e2write(parame[0][1]));
    elif(path == "/api/kafka/info"):
        api.responsing(client,getKafka.infoCollection());
    elif(path == "/api/version"):
        api.responsing(client,getKafka.getVersion());
        ##🍺操作控制器
    elif(path == "/api/action/PacketStatus"):
        api.responsing(client,actionBasic.PacketStatus());
    elif(path == "/api/action/PacketOn"):
        api.responsing(client,actionBasic.PacketOn());
    elif(path == "/api/action/PacketOff"):
        api.responsing(client,actionBasic.PacketOff());
    elif(path == "/api/action/PacketRestart"):
        api.responsing(client,actionBasic.PacketRestart());
    elif(path == "/api/action/ApiStatus"):
        api.responsing(client,actionBasic.ApiStatus());
    elif(path == "/api/action/ApiOff"):
        api.responsing(client,actionBasic.ApiOff());
    elif(path == "/api/action/KafkaStatus"):
        api.responsing(client,actionBasic.KafkaStatus());
    elif(path == "/api/action/KafkaOff"):
        api.responsing(client,actionBasic.KafkaOff());
    elif(path == "/api/action/KafkaOn"):
        api.responsing(client,actionBasic.KafkaOn());
    elif(path == "/api/action/KafkaRestart"):
        api.responsing(client,actionBasic.KafkaRestart());
    elif(path == "/api/action/MinerStatus"):
        api.responsing(client,actionBasic.MinerStatus());
    elif(path == "/api/action/MinerOn"):
        api.responsing(client,actionBasic.MinerOn());
    elif(path == "/api/action/MinerOff"):
        api.responsing(client,actionBasic.MinerOff());
    elif(path == "/api/action/MinerRestart"):
        api.responsing(client,actionBasic.MinerRestart());
    elif(path == "/api/action/ConfigStatus"):
        api.responsing(client,actionBasic.ConfigStatus());
    elif(path == "/api/action/ConfigOn"):
        api.responsing(client,actionBasic.ConfigOn());
    elif(path == "/api/action/ConfigOff"):
        api.responsing(client,actionBasic.ConfigOff());
    elif(path == "/api/action/ConfigRestart"):
        api.responsing(client,actionBasic.ConfigRestart());
    elif(path == "/api/action/AdvertiseStatus"):
        api.responsing(client,actionBasic.AdvertiseStatus());
    elif(path == "/api/action/AdvertiseOn"):
        api.responsing(client,actionBasic.AdvertiseOn());
    elif(path == "/api/action/AdvertiseOff"):
        api.responsing(client,actionBasic.AdvertiseOff());
    elif(path == "/api/action/AdvertiseRestart"):
        api.responsing(client,actionBasic.AdvertiseRestart());

##2021/12/20 ADD
    elif(path == "/api/action/FastSync"):
        api.responsing(client,actionBasic.FastSync());
    elif(path == "/api/action/Update"):
        api.responsing(client,actionBasic.FastUpdate(parame[0][1],parame[1][1]));
    elif(path == "/api/action/InstallDashboard"):
        api.responsing(client,actionBasic.InstallDashboard());
    elif(path == "/api/action/UninstallDashboard"):
        api.responsing(client,actionBasic.UninstallDashboard());
    elif(path == "/api/action/CleanBlock"):
        api.responsing(client,actionBasic.BlockClean());
    elif(path == "/api/action/MinerVersion"):
        api.responsing(client,actionBasic.MinerVersion());
    elif(path == "/api/action/DockerPs"):
        api.responsing(client,actionBasic.DockerPs());
    elif(path == "/api/action/Region"):
        api.responsing(client,actionBasic.Region());
    elif(path == "/api/action/Remote"):
        api.responsing(client,actionBasic.RemoteCmd(parame[0][1]));

        ##🍺测试接口
    elif(path == "/parame"):
        api.responsing(client,json.dumps(parame));
    else : 
        api.responsing(client,not_found());


'''
🍺路由相关controller接口集
'''
#🔥接口服务器一切正常
def index():
    ret = {'code':200,'data':"Server Alive  :-)"}
    back =json.dumps(ret)
    return back

#🔥404路径
def not_found():
    ret = {'code':404,'data':"Nothing Found Here  :-("}
    back =json.dumps(ret)
    return back

#🔥服务器错误
def server_error():
     return json.dumps({'code':500,'data':"Result Error :-("})

#🔥获取设备信息
def hotspot_info ():
    return info.getInfo();

#🔥获取设备eth0 信息
def hotspot_eth0 ():
    return getIp.networkInfo("eth0");

#🔥获取设备wlan0 信息
def hotspot_wlan0 ():
    return getIp.networkInfo("wlan0");

#🔥获取设备cpuinfo 信息
def hotspot_cpuinfo ():
    return getCpu.getHardware();

#🔥获取Miner onboading 信息
def miner_keys ():
    return getMiner.print_keys();

def provision_onboard():
    getTest.provisionEcc();
    time.sleep(3);
    return getTest.onboardingEcc()