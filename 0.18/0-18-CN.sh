echo "CN470 update"
mkdir /home/pi/hnt/script/update/
wait
mkdir /home/pi/hnt/script/update/1.08
echo "mkdir /home/pi/hnt/script/update/1.08"
wait
sudo wget https://piscesminer.oss-cn-hangzhou.aliyuncs.com/firmware/1.08/sys.config -O /home/pi/hnt/script/update/1.08/sys.config;
wait
sudo docker stop miner
wait
sudo docker rm miner
wait
echo "miner removed"
wait
sudo docker run -d --init \
--ulimit nofile=64000:64000 \
--env REGION_OVERRIDE=CN470 \
 --device /dev/i2c-0 \
 --net host \
 --restart always \
 --privileged \
 -v /var/run/dbus:/var/run/dbus \
--publish 1680:1680/udp \
--publish 44158:44158/tcp \
--name miner \
--mount type=bind,source=/home/pi/hnt/miner,target=/var/data \
--mount type=bind,source=/home/pi/hnt/script/update/1.08/sys.config,target=/config/sys.config \
quay.io/team-helium/miner:miner-arm64_2021.10.29.0_GA

wait
echo "image update success";
wait
echo "more details update"
sudo npm remove -g pm2
wait
sudo rm -rf /home/pi/api/tool/version
wait
sudo wget https://piscesminer.oss-cn-hangzhou.aliyuncs.com/firmware/1.08/version -O /home/pi/api/tool/version;
wait
echo "update 1.08 success"