#!/bin/bash 
sudo wget https://helium-snapshots.nebra.com/snap-1194112 -O /home/pi/hnt/miner/snap/latest
sudo docker exec miner miner snapshot load /var/data/snap/latest