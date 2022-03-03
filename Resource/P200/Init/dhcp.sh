#!/bin/sh


# setup network
for i in $(seq 1 1); do
  ifconfig eth$i up;
done


# setup network dhcp
for i in $(seq 1 1); do
    port=$(dhclient -i eth$i | grep Lease | awk '{print $3}')
    echo "$(date) : $port" >> /root/netdhcp.log
done