#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V2/EU868.json -O /home/pi/hnt/paket/paket/packet_forwarder/global_conf.json
wait
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V2/EU868 -O /home/pi/api/tool/region
wait
echo "EU868"