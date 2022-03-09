#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V1/global_conf.json.sx1250.IN865 -O /home/pi/hnt/paket/paket/packet_forwarder/global_conf.json
wait
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V1/EU868 -O /home/pi/api/tool/region
wait
echo "IN866"