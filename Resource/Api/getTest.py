# coding:utf-8
import os
import router
import json
import api
import RPi.GPIO as GPIO
import time

def shell(action):
    out = os.popen(action)
    info = out.read()
    return info;

def testBle():
    info =shell("hcitool dev")
    raw = info.split("Devices:")
    dev = raw[1].split("\n")
    if(len(dev)>3):
        hci1 = dev[1].split("\t")[2]
        hci0 = dev[2].split("\t")[2]
        return json.dumps({"hci0":hci0,"hci1":hci1})
    elif(len(dev)==3):
        hci0 = dev[1].split("\t")[2]
        return json.dumps({"hci0":hci0})
    else:
        return router.server_error();

def testEcc():
    info =shell("docker exec provision gateway_mfr ecc test")
    # raw = info.split("|")
    # serial_num = raw[5]
    # zone_locked_config = raw[8]
    # zone_locked_data = raw[11]
    # slot_config =raw[14]
    # key_config = raw[17]
    # miner_key = raw[20]
    #return serial_num+zone_locked_config+zone_locked_data+slot_config+key_config+miner_key
    #ret = {"serial_num":serial_num,"zone_locked_config":zone_locked_config,"zone_locked_data":zone_locked_data,"slot_config":slot_config,"key_config":key_config,"miner_key":miner_key}
    ret = {"onboarding_key":info}
    return json.dumps(ret)

def provisionEcc():
    info =shell("docker exec provision gateway_mfr ecc provision")
    # raw = info.split("|")
    # serial_num = raw[5]
    # zone_locked_config = raw[8]
    # zone_locked_data = raw[11]
    # slot_config =raw[14]
    # key_config = raw[17]
    # miner_key = raw[20]
    #return serial_num+zone_locked_config+zone_locked_data+slot_config+key_config+miner_key
    ret = {"onboarding_key":info}
    return json.dumps(ret)


def onboardingEcc():
    info =shell("docker exec provision gateway_mfr ecc onboarding")
    if (len(info)<50):
        #ecc sleep
        if(info == "ecc_asleep\n"):
            onboardingEcc()
        else:
            return json.dumps({"onboarding_key":info})
    else:
        return json.dumps({"onboarding_key":info})

##E2相关接口
def e2init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.LOW)
    return json.dumps({"code":200 , "data":"success"})

def e2write(data):
    e2init()
    time.sleep(1);
    basecmd = "i2cset -f -y 1 0x50 "
    array = e2encode(data);
    length = 14
    for ret in range(length) :
        cmd = shell(basecmd+hex(ret)+" "+array[ret]);
    return data;

def e2read():
    basecmd = "i2cget -f -y 1 0x50 "
    length = 14;
    data = [];
    for i in range(length):
        address = e2decode(i);
        cmd = shell(basecmd+address);
        ret = cmd.split("\n")[0]
        data.append(ret);
    ret = ""
    for result in data:
        ret = ret+bytes(int(result,16))
    ret = json.dumps({'minerSn':ret,'raw':data})
    return ret

def e2decode(data):
    add = int(data);
    return hex(add);

def e2encode(data):
    raw = '-'.join(data);
    data = raw.split('-');
    ff16 = [];
    for i in data:
        ff16.append(hex(int(i)))
    return ff16

def getPublicIp():
    ip = shell("curl http://debug.sidcloud.cn/ddns/index.php")
    ret = json.dumps({'PublicIp':ip})
    return ret

if __name__ == '__main__':
    print(e2read())
