sudo docker stop miner 
wait
sudo docker exec provision gateway_mfr ecc provision
wait
sudo docker start miner