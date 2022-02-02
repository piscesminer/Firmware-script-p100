#!/bin/sh 

NAME=lora_pkt_fwd

ID=`ps -ef | grep "$NAME" | grep -v "grep" | awk '{print $2}'`

echo $ID

