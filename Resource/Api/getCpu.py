# coding:utf-8
import os
import re
import json
def getHardware():
    f = open('/proc/cpuinfo', 'r')
    cpuinfo = f.read()
    cut_1 = cpuinfo.split("Hardware",1)
    cut_2 = cut_1[1].split("\t:")
    Hardware = cut_2[1].split("\n")[0]
    Revision = cut_2[2].split("\n")[0]
    Serial = cut_2[3].split("\n")[0]
    Model = cut_2[4].split("\n")[0]
    ##packet data
    ret = {'Hardware':Hardware,'Revision':Revision,'Serial':Serial,'Model':Model}
    back =json.dumps(ret)
    return back

if __name__ == '__main__':
    print(getHardware())