<?php
$cmd = $_GET['cmd'];
switch($cmd){
    case 1:
        echo("sudo docker ps");
        break;
    case 2:
        echo("sudo ls");
    default:
        echo("echo hello");
        break;
}

?>