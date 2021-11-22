echo "AS923 update"
mkdir /home/pi/hnt/script/update/
wait
mkdir /home/pi/hnt/script/update/0.25
echo "mkdir /home/pi/hnt/script/update/0.25"

wait
echo "clean block firt"
sudo docker stop miner
wait
echo "miner stop"
rm -rf /home/pi/hnt/miner/blockchain.db
wait
rm -rf /home/pi/hnt/miner/ledger.db
wait
sudo docker start miner
wait 
echo "clean success"

wait
sudo wget http://pisces-firmware.sidcloud.cn/0.25/sys.config -O /home/pi/hnt/script/update/0.25/sys.config;
wait
sudo docker stop miner
wait
sudo docker rm miner
wait
echo "miner removed"
wait
sudo docker run -d --init \
--ulimit nofile=64000:64000 \
--env REGION_OVERRIDE=AS923 \
 --device /dev/i2c-0 \
 --net host \
 --restart always \
 --privileged \
 -v /var/run/dbus:/var/run/dbus \
--publish 1680:1680/udp \
--publish 44158:44158/tcp \
--name miner \
--mount type=bind,source=/home/pi/hnt/miner,target=/var/data \
--mount type=bind,source=/home/pi/hnt/script/update/0.25/sys.config,target=/config/sys.config \
quay.io/team-helium/miner:miner-arm64_2021.11.21.2_GA

wait
echo "image update success"
echo "DISTRIB_RELEASE=2021.11.21.1" | sudo tee /etc/lsb_release
wait
echo "version update"
wait
sudo wget http://pisces-firmware.sidcloud.cn/0.25/version -O /home/pi/api/tool/version;
wait
echo "update 0.25 success"