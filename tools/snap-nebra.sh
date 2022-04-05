#!/bin/bash 
sudo wget https://helium-snapshots.nebra.com/snap-1298596 -O /home/pi/hnt/miner/snap/latest
sudo docker exec miner miner snapshot load /var/data/snap/latest