sudo docker stop miner 
wait
sudo docker exec provision gateway_mfr ecc provision_onboard
wait
sudo docker start miner
wait
sudo docker exec miner miner print_keys > /home/pi/hnt/miner/public_keys
wait
cat /home/pi/hnt/miner/public_keys
