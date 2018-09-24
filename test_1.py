'''a = 1

def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fib(n-1) + fib(n-2) 

a = input("请输入你要的数字：")	
	
print(fib(int(a)))	



def hano(n,a,b,c):
	
	if n == 1:
		print(a,"--->",c)
		return None
	if n == 2:
		print(a,"--->",b)
		print(a,"--->",c)
		print(b,"--->",c)
		return None
	hano(n-1,a,c,b)
	hano(n-1,b,a,c)
a = "A"
b = "B"
c = "C"
n = 5
hano(n,a,b,c)	

a = (["sds",1],["sdbhs",2],["xsx",3],["vf",4])
for k,v in a:
	print(k,"---",v)
'''
'''

#消耗内存资源的一种排序方式
a = [2,5,4,4,5,6,6,5,7]
b = []
c = 0
d = len(a) - 1
while c <= d:
	b.append(max(a))
	a.remove(max(a))
	c += 1
print(b)

#封装成一个函数
def pai_xu(a):
	b = []
	c = 0
	d = len(a) - 1
	while c <= d:
		b.append(max(a))
		a.remove(max(a))
		c += 1
	return b

a = [2,5,4,4,5,6,6,5,7]
print(pai_xu(a))
'''


	
class PythonStudent():
	
	name = None
	age = 18
	course = "Python"
	
	def dohomework(self):
		
		print("在写作业")
		
		return None
PythonStudent.__dict__	
tuii = PythonStudent()

tuii.__dict__


'''
conda list
conda env list
conda creat -n XXX python=3.7
'''









