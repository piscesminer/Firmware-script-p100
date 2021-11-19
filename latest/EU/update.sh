echo "Eu868 update"
mkdir /home/pi/hnt/script/update/
wait
mkdir /home/pi/hnt/script/update/0.23
echo "mkdir /home/pi/hnt/script/update/0.23"
wait
sudo wget http://pisces-firmware.sidcloud.cn/0.23/sys.config -O /home/pi/hnt/script/update/0.23/sys.config;
wait
sudo docker stop miner
wait
sudo docker rm miner
wait
echo "miner removed"
wait
sudo docker run -d --init \
--ulimit nofile=64000:64000 \
 --device /dev/i2c-0 \
 --net host \
 --restart always \
 --privileged \
 -v /var/run/dbus:/var/run/dbus \
--publish 1680:1680/udp \
--publish 44158:44158/tcp \
--name miner \
--mount type=bind,source=/home/pi/hnt/miner,target=/var/data \
--mount type=bind,source=/home/pi/hnt/script/update/0.23/sys.config,target=/config/sys.config \
quay.io/team-helium/miner:miner-arm64_2021.11.17.2_GA

wait
echo "image update success"
echo "DISTRIB_RELEASE=2021.11.17.2" | sudo tee /etc/lsb_release
wait
echo "version update"
wait
sudo wget http://pisces-firmware.sidcloud.cn/0.23/version -O /home/pi/api/tool/version;
wait
echo "update 0.23 success"