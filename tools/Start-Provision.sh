echo "start provision"
sudo docker run -d --device /dev/i2c-0:/dev/i2c-1 --name provision gateway_mfr:arm64
wait
echo "success"