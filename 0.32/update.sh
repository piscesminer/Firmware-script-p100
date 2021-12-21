#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/actionBasic.py  -O /home/pi/api/actionBasic.py
wait
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/router.py  -O /home/pi/api/router.py
wait
sudo wget http://pisces-firmware.sidcloud.cn/Resource/Api/region -O /home/pi/api/tool/region
wait
echo "version update"
wait
sudo wget http://pisces-firmware.sidcloud.cn/0.32/version -O /home/pi/api/tool/version;
wait
echo "update 0.32 success"
