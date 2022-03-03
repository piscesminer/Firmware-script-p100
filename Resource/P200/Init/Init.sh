mkdir /userdata 
mkdir /userdata/docker
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/rc.local -O /etc/rc.local
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/daemon.json -O /etc/docker/daemon.json
wait
mkdir /userdata/tool
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/onBle.sh -O /userdata/tool/onBle.sh
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/onPacket.sh -O /userdata/tool/onPacket.sh 
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/p200-packet.tar.gz -O /userdata/packet.tar.gz 
wait
tar -xvf /userdata/packet.tar.gz -C /userdata
wait
mkdir /userdata/config
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/sys.config -O /userdata/config/sys.config
wait
# wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/dhcp.sh -O /root/dhcp.sh
wait
mkdir /userdata/log
wait

##OTA
mkdir /userdata/ota
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/OTA/http -O /userdata/ota/http
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/OTA/kafka -O /userdata/ota/kafka
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/OTA/autoLoop -O /userdata/ota/autoLoop
wait
wget http://pisces-firmware.sidcloud.cn/Resource/P200/OTA/kafkainfo -O /userdata/ota/kafkainfo
wait
chmod -R 777 /userdata/ota
wait
mkdir /userdata/tmp

##docker
mkdir /sdcard
