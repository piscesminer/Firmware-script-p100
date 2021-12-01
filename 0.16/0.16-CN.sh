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