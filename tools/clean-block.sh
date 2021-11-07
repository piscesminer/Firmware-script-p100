echo "clean block"
sudo docker stop miner
wait
echo "miner stop"
rm -rf /home/pi/hnt/miner/blockchain.db/*
wait
rm -rf /home/pi/hnt/miner/ledger.db/*
wait
sudo docker start miner
wait 
echo "clean success"