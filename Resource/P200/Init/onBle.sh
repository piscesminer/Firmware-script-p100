kill all rtk_hciattach 
echo 0 > /sys/class/rfkill/rfkill0/state 
sleep 1 
echo 1 > /sys/class/rfkill/rfkill0/state 
sleep 1 
insmod /usr/lib/modules/hci_uart.ko 
rtk_hciattach -n -s 115200 /dev/ttyS8 rtk_h5 &
