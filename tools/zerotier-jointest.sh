sudo rm -rf /var/lib/zerotier-one/
wait
sudo apt remove zerotier-one -y
wait
sudo apt install zerotier-one
wait
sudo zerotier-cli join a09acf0233ae6dbf
echo "join success"