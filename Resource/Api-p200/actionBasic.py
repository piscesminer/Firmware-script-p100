# coding:utf-8
import os
import json
import RPi.GPIO as GPIO
import time

def shell(action):
    out = os.popen(action)
    info = out.read()
    return info;

def PacketStatus():
    status = shell("sudo bash /userdata/api/tool/getPacket.sh").split("\n")[0]
    return status

def PacketOn():
    status = PacketStatus();
    if(status):
        return "running:"+status
    else:
        shell("sudo bash /api/tool/onPacket.sh")
        return "succes"

def PacketOff():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 

def PacketRestart():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        time.sleep(0.3);
        PacketRestart();
    else:
        PacketOn();
        return "not running" 

def ApiStatus():
    status = shell("sudo netstat -anp|grep 8001|awk '{printf $7}'|cut -d/ -f1")
    return status

def ApiOff():
    status = apiStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 
        

def KafkaStatus():
    status = shell("sudo netstat -anp|grep 8002|awk '{printf $7}'|cut -d/ -f1")
    return status

def KafkaOn():
    status = KafkaStatus();
    if(status):
        return "running:"+status
    else:
        shell("sudo node userdata/kafka/kafka.js > userdata/log/kafka.log &")
        return "succes"
def KafkaOff():
    status = KafkaStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 

def KafkaRestart():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        time.sleep(0.3);
        KafkaRestart();
    else:
        KafkaOn();
        return "not running" 

def MinerStatus():
    status = shell("sudo docker inspect --format '{{.Name}} {{.State.Running}}' miner ");
    return status

def MinerOn():
    shell("sudo docker start miner ");
    return true

def MinerOff():
    return shell("sudo docker stop miner");

def MinerRestart():
    return shell("sudo docker restart miner")

def ConfigStatus():
    status = shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config ping").split("\n")[0]
    if(status == "pong"):
        return "runing"
    else:  
        return status

def ConfigOn():
    status = ConfigStatus();
    if(status=="runing"):
        return "running:"+status
    else:
        shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config start")
        return "succes"

def ConfigOff():
    status = KafkaStatus();
    if(status=="runing"):
        shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config stop")
        return("stop "+status)
    else:
        return "not running" 

def ConfigRestart():
    status = ConfigStatus();
    if(status=="runing"):
        ConfigOff()
        time.sleep(0.3);
        ConfigRestart();
    else:
        ConfigOn();
        return "not running" 


def AdvertiseStatus():
    status = shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config advertise status").split("\n")[0]
    return status

def AdvertiseOn():
    status = AdvertiseStatus();
    if(status=="off"):
        shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config advertise on")
        return "running:"+status
    else:
        return "succes"

def AdvertiseOff():
    status = AdvertiseStatus();
    if(status=="on"):
        shell("sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config off")
        return("stop "+status)
    else:
        return "not running" 

def AdvertiseRestart():
    status = AdvertiseStatus();
    if(status=="off"):
        AdvertiseOn();
    else:
        AdvertiseOff()
        time.sleep(0.3);
        AdvertiseRestart();
        return "not running" 


## New Actions: ##2021/12/20
def FastSync():
    status = shell("sudo wget https://pisces-snap.sidcloud.cn/snap/snap-update.sh -O - | sudo bash")
    return status;
def FastUpdate(region,version):
    print(version);
    status = shell("sudo wget http://pisces-firmware.sidcloud.cn/"+version+"/"+region+"/update.sh -O - | sudo bash")
    return status;
def InstallDashboard():
    status = shell("sudo wget https://raw.githubusercontent.com/briffy/PiscesQoLDashboard/main/install.sh -O - | sudo bash")
    return status;
def UninstallDashboard():
    status = shell("sudo bash /var/dashboard/uninstall.sh -y")
    return status;
def BlockClean():
    status = shell("sudo wget http://pisces-firmware.sidcloud.cn/tools/clean-block.sh -O - | sudo bash")
    return status;
def MinerVersion():
    status = shell('sudo docker ps --format "{{.Image}}" --filter "name=miner" | grep -Po "miner-arm64_.*"')
    return status;
def DockerPs():
    status = shell('sudo docker ps')
    return status;
def Region():
    f = open('userdata/api/tool/region', 'r')
    region = f.read()
    return region;
def RemoteCmd(cmd):
    status = shell("sudo wget http://pisces-firmware.sidcloud.cn/tools/Remote.php?cmd="+cmd+" -O - | sudo bash")
    return status;
# print(AdvertiseStatus())