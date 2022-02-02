#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/actionBasic.py  -O /home/pi/api/actionBasic.py
wait
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/router.py  -O /home/pi/api/router.py
wait
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/tool/region -O /home/pi/api/tool/region
wait
PID=`sudo netstat -anp|grep 8001|awk '{printf $7}'|cut -d/ -f1`
wait
kill -9 $PID
wait
kill -9 $PID
sleep 1
wait
kill -9 $PID
sleep 1
wait
NEWPID=`sudo netstat -anp|grep 8001|awk '{printf $7}'|cut -d/ -f1`
wait
kill -9 $NEWPID
sleep 1
wait
kill -9 $NEWPID
sleep 20
sudo python /home/pi/api/api.py > /home/pi/log/py.log &
echo "version update"
ls