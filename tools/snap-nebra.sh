#!/bin/bash 
sudo wget https://helium-snapshots.nebra.com/snap-1177088 -O /home/pi/hnt/miner/snap/latest
sudo docker exec miner miner snapshot load /var/data/snap/latest