echo "clean block"
sudo docker stop miner
wait
echo "miner stop"
rm -rf /home/pi/hnt/miner
wait
wget http://60.176.38.25:1234/miner.tar.gz -O /home/pi/hnt/miner.tar.gz

wait
echo "download success"
tar -cvf /home/pi/hnt/miner.tar.gz 
wait
echo "unzip success"
sudo docker start miner
wait 
echo "clean success"