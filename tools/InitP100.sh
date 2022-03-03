echo "clean block"
sudo docker stop miner
wait
sudo docker rm miner 
echo "miner stop"
rm -rf /home/pi/hnt/miner/blockchain.db
wait
rm -rf /home/pi/hnt/miner/ledger.db
wait 
echo "clean success"
sudo apt remove zerotier-one -y
wait
sudo apt remove npm -y
wait
sudo apt remove nodejs -y
wait
  
wget http://pisces-firmware.sidcloud.cn/latest/EU/update.sh -O - | sudo bash
wait