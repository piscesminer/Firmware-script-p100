#!/bin/sh

# set -x
# Exit with error if some command fails
# set -e

FIRMWARE_VERSION="0.30"
FIRMWARE_CONFIG_PATH="/home/pi/hnt/miner/configs/"
MINER_DOCKER_VERSION="miner-arm64_2021.12.09.0_GA"

SYSTEM=`sudo docker ps --format "{{.Image}}" --filter "name=miner" | grep -Po "miner-arm64_.*"`
if [ $SYSTEM = $MINER_DOCKER_VERSION ] ; then 
echo "❌Aleady update"
else
echo "🍺Running $MINER_DOCKER_VERSION image"
fi     #ifend