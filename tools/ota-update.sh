echo "version 1.06 updating" > /home/pi/log/update-1-06.log ;
wait;
sudo rm -rf /home/pi/kafka.zip ;
wait;
echo "kafka remove successed" > /home/pi/log/update-1-06.log ;
wait;
sudo wget https://pisces-snap.sidcloud.cn/ota-update/kafka.zip -O /home/pi/kafka.zip;
wait;
sudo rm -rf /home/pi/kafka ;
wait;
echo "kafka download successed" > /home/pi/log/update-1-06.log ;
wait;
sudo unzip -o /home/pi/kafka.zip -d /home/pi ;
wait;
echo "kafka update successed" > /home/pi/log/update-1-06.log ;
wait;
sudo wget https://pisces-snap.sidcloud.cn/ota-update/init.sh -O /home/pi/hnt/script/init.sh;
wait;
echo "init.sh update success" > /home/pi/log/update-1-06.log ;
sudo rm -rf /home/pi/kafka.zip ;
wait;
echo "version 1.06 update successed" > /home/pi/log/update-1-06.log ;