echo "remove provision"
sudo docker stop provision
wait
sudo docker rm provision
wait
echo "success"