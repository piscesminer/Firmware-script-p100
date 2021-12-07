#!/bin/bash

# Echoes executed command
set -x
# Exit with error if some command fails
set -e

FIRMWARE_VERSION="0.27"
FIRMWARE_CONFIG_PATH="/home/pi/hnt/script/update/$FIRMWARE_VERSION"
MINER_DOCKER_VERSION="miner-arm64_2021.11.29.0"

echo "Eu868 update $FIRMWARE_VERSION"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

mkdir -p "$FIRMWARE_CONFIG_PATH"

# Download config first to avoid stopping container if fails
# Do not write sys.config if 404 error
curl -Lf "http://pisces-firmware.sidcloud.cn/$FIRMWARE_VERSION/sys.config" -o "$FIRMWARE_CONFIG_PATH/sys.config"

# Stop miner container if already started
docker stop miner || true 
docker rm miner || true 

# echo "Cleaning blocks"
# rm -rf "/home/pi/hnt/miner/blockchain.db/*"
# rm -rf "/home/pi/hnt/miner/ledger.db/*"

echo "Running $MINER_DOCKER_VERSION image"

# As it runs with "host" network no need to expose ports
docker run -d --init \
    --ulimit nofile=64000:64000 \
    --env REGION_OVERRIDE=CN470 \
    --device /dev/i2c-0 \
    --net host \
    --restart always \
    --privileged \
    -v /var/run/dbus:/var/run/dbus \
    --name miner \
    --publish 1680:1680/udp \
    --publish 44158:44158/tcp \
    --mount type=bind,source=/home/pi/hnt/miner,target=/var/data \
    --mount type=bind,source="$FIRMWARE_CONFIG_PATH/sys.config",target=/config/sys.config \
    "quay.io/team-helium/miner:$MINER_DOCKER_VERSION"

echo "Container miner running and updated"
echo "DISTRIB_RELEASE=2021.11.29.0" | sudo tee /etc/lsb_release
wait
echo "version update"
wait
sudo wget http://pisces-firmware.sidcloud.cn/$FIRMWARE_VERSION/version -O /home/pi/api/tool/version;
wait
echo "update $FIRMWARE_VERSION success"
