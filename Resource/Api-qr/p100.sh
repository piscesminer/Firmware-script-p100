wget https://pisces-snap.sidcloud.cn/api/qrcode -O /home/pi/api/tool/qrcode
wait
chmod -R 777 /home/pi/api/tool/qrcode
wait
echo "/home/pi/api/tool/qrcode &" >> /home/pi/hnt/script/init.sh
wait
/home/pi/api/tool/qrcode &