#!/bin/bash

# Echoes executed command
# set -x
# Exit with error if some command fails
# set -e

FIRMWARE_VERSION="0.60"

GATEWAY_RS_PATH="/etc/helium_gateway/"
REGION = "AS"

echo "update $FIRMWARE_VERSION"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi





# echo "Cleaning blocks"
# rm -rf "/home/pi/hnt/miner/blockchain.db/*"
# rm -rf "/home/pi/hnt/miner/ledger.db/*"
mkdir -p "$GATEWAY_RS_PATH"
rm -rf "$GATEWAY_RS_PATH/*"

# Download the gateway_rs programe
wget "https://github.com/helium/gateway-rs/releases/download/v1.0.0/helium-gateway-1.0.0-armv7-unknown-linux-musleabihf.tar.gz -P $GATEWAY_RS_PATH"
wait
# Unzip the pack
tar -xvf "$GATEWAY_RS_PATH/helium-gateway-1.0.0-armv7-unknown-linux-musleabihf.tar.gz" -C "$GATEWAY_RS_PATH"
wait

# Download config
curl -Lf "http://pisces-firmware.sidcloud.cn/$FIRMWARE_VERSION/$REGION/setting.toml" -o "$GATEWAY_RS_PATH/setting.toml"
# export PATH=/root/update/:$PATH

# Download the service 
curl -Lf "http://pisces-firmware.sidcloud.cn/$FIRMWARE_VERSION/helium.service" -o "/lib/systemd/system/helium.service"

# Stop miner container if already started
    docker stop miner || true 
    docker rm miner || true 
# Stop the service of helium
    service helium stop 

# Start up the service
    service helium start

echo "Helium_gateway running and updated"

# Update the lsb_release file
fi     #ifend
echo "DISTRIB_RELEASE=2023.03.30" | sudo tee /etc/lsb_release
wait
echo "version update"
wait

# Update the version file
sudo wget http://pisces-firmware.sidcloud.cn/$FIRMWARE_VERSION/version -O /home/pi/api/tool/version;
wait
echo "update $FIRMWARE_VERSION success"