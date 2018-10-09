import os

def findfile(target,target_path):
	area = os.listdir(target_path)		
	for f in area:
		if target in f:
			print("------" + f + "-------" + "\n" + target_path + '/' + f)
		elif not '.' in f:
			new_path = target_path
			new_path += '/' +f
			findfile(target,new_path) 			
while True:
	try:
		path = os.getcwd()			
		print("这是当前路径：" + path)
		wewant = input("请输入想要找到的文件，越详细越好：")
		findfile(wewant,path)			
	except NotADirectoryError:
		print("抱歉，部分路径没有权限！")