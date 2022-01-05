
echo "Update the patch"
sudo docker pull ghcr.io/heliumdiy/helium_workarounds:latest
wait
sudo docker run -d --init \
    --name workaround \
    --mount type=bind,source=/home/pi/hnt/miner/log,target=/log \
    ghcr.io/heliumdiy/helium_workarounds