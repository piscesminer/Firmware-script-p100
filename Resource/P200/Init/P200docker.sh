docker run -d --init \
    --ulimit nofile=64000:64000 \
    --device /dev/i2c-2 \
    --net host \
    --restart always \
    --privileged \
    --name miner \
    --publish 127.0.0.1:1680:1680/udp \
    --publish 44158:44158/tcp \
    --mount type=bind,source=/sdcard/miner,target=/var/data \
    --mount type=bind,source=/userdata/log,target=/var/log/miner \
    --mount type=bind,source="/userdata/config/sys.config",target=/config/sys.config \
    "quay.io/team-helium/miner:miner-arm64_2022.01.29.0_GA"


wget https://helium-media.s3-us-west-2.amazonaws.com/gateway_mfr-aarch64.tar -O /userdata/tmp/gateway_mfr-aarch64.tar 

docker load -i /userdata/tmp/gateway_mfr-aarch64.tar 

docker run -d --device /dev/i2c-2:/dev/i2c-1 --name provision gateway_mfr:arm64