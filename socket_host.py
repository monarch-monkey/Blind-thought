import socket
import sys

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host,port))
serversocket.listen(5)
print("链接服务在线！请开启客户端连接！")

while True:
	
	clientsocket,addr = serversocket.accept()
	print("链接地址：%s" % str(addr))
	msg = "这是一条来自服务器的消息，不要回答！"
	clientsocket.send(msg.encode('utf-8'))	
	clientsocket.close()
	
	
