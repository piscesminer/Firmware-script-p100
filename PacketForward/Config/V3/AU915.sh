#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/global_conf.json.sx1250.AU915V3 -O /home/pi/hnt/paket/paket/packet_forwarder/global_conf.json
wait
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/AU915 -O /home/pi/api/tool/region
wait
echo "AU915"