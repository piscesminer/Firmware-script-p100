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
tar -cvf /userdata/packet.tar.gz 
wait
mkdir /userdata/config
wget http://pisces-firmware.sidcloud.cn/Resource/P200/Init/sys.config -O /userdata/config/sys.config