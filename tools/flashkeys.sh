
sudo docker stop miner 
wait
sudo docker exec provision gateway_mfr ecc provision_onboard
wait
sudo docker start miner
wait