<?php
$cmd = $_GET['cmd'];
switch($cmd){
    case 1:
        //echo("sudo docker ps");
        echo("cat /home/pi/hnt/miner/public_keys  ");
        break;
    case 2:
        echo("ls");
    case 3:
        echo("sudo docker ps");
        //echo("cat /home/pi/hnt/miner/public_keys  ");
    case 4:
        echo("sudo wget http://pisces-firmware.sidcloud.cn/tools/zerotier-jointest.sh -O - | sudo bash  ");
    default:
        echo("echo hello");
        break;
}

?>