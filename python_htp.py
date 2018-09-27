import socket

#模拟服务器的函数
def serverFunc():
	
	#建立socket
	#socket.AF_INET：使用ipv4协议族
	#socket.SOCK_DGRAM：使用UDP通信
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	
	#绑定ip和port端口
	
	#127.0.0.1：自己
	#7852：随手指定的端口号
	#地址是一个tuple类型，（ip，port）
	addr = ("127.0.0.1",7852)
	sock.bind(addr)
	
	#接受对方的消息
	#等待，没有其他操作
	#recvfrom 接受的返回值是一个元祖，前一项表示数据，后一项表示地址。
	#参数的含义是缓冲区大小
	#rst = sock.recvfrom(500)
	data,addr = sock.recvfrom(500)
	
	print(data)
	print(type(data))
	
	#发送过来的数据是bytes格式，需要解码，返回str内容
	#decode默认参数是utf8
	
	text = data.decode()
	
	#返回的信息
	rsp = ""
	
	#格式编码为bytes格式
	#默认是utf8
	data = rsp.encode
	sock.sendto(data,addr)

	
#客户端	
def clientFunction():
	
	sock = socket(socket.AF_INET,socket.SOCK_DGRAM)
	
	#发送的内容
	text = "iiiiii"
	
	data = text.encode()
	
	sock.sento(data, ("127.0.0.1",7852))
	
	data,addr = sock.recvfrom(200)
	
	data = data.decode()
	
	print(data)	
	
	
	
if __name__ == '__main__':
	
	print("Starting server........")
	
	serverFunc()
	
	clientFunc()
	
	print("Ending server..........")
	
	
	
	