#! /bin/bash
sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config start 
sleep 1
sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config ping > userdata/log/gateway_config.log
sleep 1
sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config advertise on > userdata/log/advertise.on.log
sleep 1
time1=$(date)
sudo echo $time1 > userdata/log/advertise_time.log
sudo userdata/config/_build/prod/rel/gateway_config/bin/gateway_config advertise status > userdata/log/advertise.log
