#! /bin/bash
sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config start 
sleep 1
sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config ping > /home/pi/log/gateway_config.log
sleep 1
sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config advertise on > /home/pi/log/advertise.on.log
sleep 1
time1=$(date)
sudo echo $time1 > /home/pi/log/advertise_time.log
sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config advertise status > /home/pi/log/advertise.log
