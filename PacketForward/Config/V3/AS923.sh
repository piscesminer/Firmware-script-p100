#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/global_conf.json.sx1250.AS923_1V3 -O /home/pi/hnt/paket/paket/packet_forwarder/global_conf.json
wait
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/AS923 -O /home/pi/api/tool/region
wait
echo "US915"