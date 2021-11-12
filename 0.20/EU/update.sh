echo "Eu868 update"
mkdir /home/pi/hnt/script/update/
wait
mkdir /home/pi/hnt/script/update/1.09
echo "mkdir /home/pi/hnt/script/update/1.09"
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
quay.io/team-helium/miner:miner-arm64_2021.11.10.0_GA

wait
# echo "image update success"
# wait
# echo "more details update"

# echo "clean dashboard"
# wget  http://pisces-firmware.sidcloud.cn/dashboard/uninstall-dashboard.sh -O - | sudo bash
# wait
echo "update dashboard"
wget https://raw.githubusercontent.com/briffy/PiscesQoLDashboard/main/install.sh -O - | sudo bash
wait
echo "update dashboard over"
wait
echo "clean block"
wget http://pisces-firmware.sidcloud.cn/tools/clean-block.sh -O - | sudo bash
wait
echo "rm provision"
wget http://pisces-firmware.sidcloud.cn/tools/remove-provision.sh -O - | sudo bash
wait
sudo wget http://pisces-firmware.sidcloud.cn/0.20/version -O /home/pi/api/tool/version;
wait
echo "update 1.09 success"