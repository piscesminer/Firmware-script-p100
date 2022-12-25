sudo docker stop miner
wait
sudo docker rm miner
wait
docker run -d --init \
    --ulimit nofile=64000:64000 \
    --device /dev/i2c-2 \
    --net host \
    --restart always \
    --privileged \
    --name miner \
    --publish 127.0.0.1:1680:1680/udp \
    --publish 44158:44158/tcp \
    --mount type=bind,source="/userdata/config/sys.config",target=/config/sys.config \
    "quay.io/team-helium/miner:miner-arm64_2022.10.28.0_GA"