#!/bin/bash 
dating" > /home/pi/log/snap-update-begain.log ;
wait
sudo wget https://helium-snapshots.nebracdn.com/snap-1475863.gz -O /home/pi/hnt/miner/snap/snap-latest;
wait
echo "download success" > /home/pi/log/snap-update-wget.log ;
wait
sudo docker exec miner miner snapshot load /var/data/snap/snap-latest;
wait
echo "update success" > /home/pi/log/snap-update-end.log ;