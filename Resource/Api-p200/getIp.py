# coding:utf-8
import  os
import  sys
import json

try :
     import  netifaces
except  ImportError:
     try :
         command_to_execute  =  "pip install netifaces || easy_install netifaces"
         os.system(command_to_execute)
     except  OSError:
         print  "Can NOT install netifaces, Aborted!"
         sys.exit( 1 )
     import  netifaces


def networkInfo(dev):
    #print(netifaces.gateways())
    routingGateway  =  netifaces.gateways()[ 'default' ][netifaces.AF_INET][ 0 ]
    routingNicName  =  dev
    #print(routingNicName)
    for  interface  in  netifaces.interfaces():
         if  interface  ==  routingNicName:
             routingNicMacAddr  =  netifaces.ifaddresses(interface)[netifaces.AF_LINK][ 0 ][ 'addr' ]
             try :
                 routingIPAddr  =  netifaces.ifaddresses(interface)[netifaces.AF_INET][ 0 ][ 'addr' ]
             except  KeyError:
                pass
    display_format  =  '%-30s %-20s'
    
    # print  display_format  %  ( "Routing NIC Name:" , routingNicName)
    # print  display_format  %  ( "Routing NIC MAC Address:" , routingNicMacAddr)
    if(dev == 'eth0'):
        # print  display_format  %  ( "Routing IP Address:" , routingIPAddr)
        # print  display_format  %  ( "Routing Gateway:" , routingGateway)
       return jsonType (routingNicName,routingNicMacAddr,routingIPAddr,routingGateway)
    else :
       return jsonType (routingNicName,routingNicMacAddr,"",routingGateway)
  #  print  display_format  %  ( "Routing IP Netmask:" , routingIPNetmask)


def jsonType (routingNicName,routingNicMacAddr,routingIPAddr,routingGateway):
    ret = {'NicName':routingNicName,'MacAddress':routingNicMacAddr,'IpAddress':routingIPAddr,'Gateway':routingGateway}
    back =json.dumps(ret)
    return back


if __name__ == '__main__':
    print(networkInfo("eth0"))
    print(networkInfo("wlan0"))
