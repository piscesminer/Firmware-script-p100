#!/bin/bash
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/IN868.json -O /home/pi/hnt/paket/paket/packet_forwarder/global_conf.json
wait
sudo wget http://pisces-firmware.sidcloud.cn/PacketForward/Config/V3/IN868 -O /home/pi/api/tool/region
wait
echo "In868"