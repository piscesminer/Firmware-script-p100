# coding:utf-8

import os
import sys
import json
import router

# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
 
# Return RAM information (unit=kb) in a list                                       
# Index 0: total RAM                                                               
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
 
# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("sudo bash ./tool/cpuUsage.sh").readline().strip()))
 
# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                         
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used                                                  
def getDiskSpace():
    p = os.popen("df -m /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
 
 
# CPU informatiom
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()
 
# RAM information
# Output is in kb, here I convert it in Mb for readability
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)
 
# Disk information
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_used = DISK_stats[1]
DISK_perc = DISK_stats[3]
 


'''
init function
'''

def init():
    global CPU_temp
    global CPU_usage
    global RAM_stats
    global RAM_total
    global RAM_used
    global RAM_free
    global DISK_stats
    global DISK_total
    global DISK_used
    global DISK_perc
    CPU_temp = getCPUtemperature()
    CPU_usage = getCPUuse()
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000,1)
    RAM_used = round(int(RAM_stats[1]) / 1000,1)
    RAM_free = round(int(RAM_stats[2]) / 1000,1)
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3].split("%")[0]
    return jsonType(CPU_temp,CPU_usage,str(RAM_total),str(RAM_used),str(RAM_free),str(DISK_total),str(DISK_used),str(DISK_perc))



def jsonType (CpuTemp,CpuUsage,RamTotal,RamUsed,RamFree,DiskTotal,DiskUsed,DiskPerc):
    ret = {'CpuTemp':CpuTemp,'CpuUsage':CpuUsage,'RamTotal':RamTotal,'RamUsed':RamUsed,'RamFree':RamFree,'DiskTotal':DiskTotal,'DiskUsed':DiskUsed,'DiskPerc':DiskPerc}
    back =json.dumps(ret)
    return back

def getInfo():
    return init()

if __name__ == '__main__':
    #jsonType(CPU_temp,CPU_usage,str(RAM_total),str(RAM_used),str(RAM_free),str(DISK_total),str(DISK_used),str(DISK_perc))
    getInfo()
