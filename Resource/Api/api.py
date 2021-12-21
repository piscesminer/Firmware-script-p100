# coding:utf-8

import socket
import router

from multiprocessing import Process

'''
🍺数据转义字典
'''
def decode(data):
    ret = data.replace("%20", " ")
    print(ret);
    return ret
'''
🍺路由前置接口
对路由进行解包。并进行分发
'''
def getRoute( client ,request_data):
    raw = request_data.split("HTTP",2)
    route = raw[0].split(" ",2)
    method = route[0]
    path = route[1].split("?")[0]
    parames = ""

    if(len(route[1].split("?"))>1):
        parames = route[1].split("?")[1]
        devpar = parames.split("&");
        parames = []
        for list in devpar:
            listcut = list.split("=")
            for i in range(0, len(listcut)): 
                listcut[i] = decode(listcut[i])
            parames.append(listcut)

    print(path)
    #responsing( client , path);
    router.router(client,method,path,parames)

'''
🍺相应函数
向客户端返回对应内容data
'''
def responsing(client,data):
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = data
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向客户端返回响应数据
    client.send(bytes(response))
    # 关闭客户端连接
    client.close()

'''
🍺处理客户端请求
获取客户端信息并转发到路由
'''

def handle_client(client_socket):

    request_data = client_socket.recv(1024)
    #print("request data:", request_data)
    getRoute(client_socket ,request_data)

'''
🍺主函数
用于启动Http服务器初始化等
'''
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8001))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()