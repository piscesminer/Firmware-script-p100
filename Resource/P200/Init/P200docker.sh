docker run -d --init \
    --ulimit nofile=64000:64000 \
    --device /dev/i2c-0 \
    --net host \
    --restart always \
    --privileged \
    -v /var/run/dbus:/var/run/dbus \
    --name miner \
    --publish 127.0.0.1:1680:1680/udp \
    --publish 44158:44158/tcp \
    --mount type=bind,source=/home/pi/hnt/miner,target=/var/data \
    --mount type=bind,source=/home/pi/hnt/miner/log,target=/var/log/miner \
    --mount type=bind,source="/userdata/config/sys.config",target=/config/sys.config \
    "quay.io/team-helium/miner:miner-arm64_2022.01.29.0_GA"