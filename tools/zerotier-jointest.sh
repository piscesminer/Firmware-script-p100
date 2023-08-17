sudo rm -rf /var/lib/zerotier-one/
wait
sudo apt remove zerotier-one -y
wait
sudo apt install zerotier-one
wait
sudo zerotier-cli join af415e486fd2a14e
echo "join success"