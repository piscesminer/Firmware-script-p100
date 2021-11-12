echo "Eu868 update"
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
--mount type=bind,source=/home/pi/hnt/script/sys.config,target=/opt/miner/releases/2021.09.16.1/sys.config \
quay.io/team-helium/miner:miner-arm64_2021.09.16.1

echo "version update"
wait
sudo rm -rf /home/pi/api/tool/version
wait
sudo wget https://piscesminer.oss-cn-hangzhou.aliyuncs.com/firmware/1.08/version -O /home/pi/api/tool/version;
wait
echo "update 1.06 success"