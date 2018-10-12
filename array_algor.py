

def print_list(l):
	'''
	展开一个嵌套的列表
	'''
	for i in l:		
		if type(i) != list: 
			print(i)
		else:
			print_list(i)
			
#target = [2,[2,5,[6,7,[5,6,78]]]]			
#print_list(target)			


			
#删除重复元素
def remove_0(list):
	list = list(set(list))
	return(list)
	
def remove_1(nums):
	i = 0
	nums.sort()
	while i < len(nums)-1:
		if nums[i] == nums[i+1]:
			nums.remove(nums[i]);
		else:
			i = i+1;
	return nums	

	
'''	
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。	
'''



def get_more(num):
	sum = 0
	i = 0
	while i < len(num)-1:
		if num[i] < num[i+1]:
			sum += num[i+1] - num[i]
			i += 2
		else :
			i += 1
	return sum		
'''

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
'''

def move_1(num,kn):
	a = []
	k = kn
	if k < len(num):	
		for i in range((k)):
			a.append(num[-i-1]) 
		for i in range((k)):
			num.pop()
		a += num
	elif k%len(num) == 0:
		a = num
	else:
		c = k % len(num)
		for i in range((c)):
			a.append(num[-i-1]) 
		for i in range((c)):
			num.pop()
		a += num		
	return a

'''	
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
'''

def relist(li):
	a = list(set(li))
	if len(a) < len(li):
		return True
	else:
		return False

'''	
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？	
'''	
#具有线性时间复杂度
def findone(num):
	for n in num:
		if num.count(n) == 1:
			return n 

def findone_1(num):
	num.sort()
	for i in range(len(num)):
		if len(num) == 1:
			return num[0]
		if num[0] == num[1]:
			num.remove(num[0])
			num.remove(num[0])
		else:
			return num[0]
'''			
给定两个数组，编写一个函数来计算它们的交集。		

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
def jiaoji(num1,num2):
	num_new = []
	num = list(set(num1+num2))
	for n in num:
		if n in num1 and n in num2:
			num_new.append(n)
	num.clear()		
	for i in num_new:
		if 	num1.count(i) == 1 or num2.count(i) ==1:
			num.append(i)
		else:	
			if num1.count(i) <= num2.count(i):
				for a in range(num1.count(i)):
					num.append(i)
			elif num1.count(i) > num2.count(i):
				for a in range(num2.count(i)):
					num.append(i)
	return num	

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
'''
num = [9,9,9,9]

def add_num(num):
	math = 0
	new = []
	for i in range(len(num)):
		math += num[-1-i]*(10**i)
	math += 1
	new = list(map(int,str(math)))
	return new		

'''	
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。	
'''		
def zero_move(num):
	for n in num:
		if n == 0:
			num.remove(n)
			num.append(0)
	return num	
	
'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

list = [1,5,9,6,5,3,9]
num = 11
'''
def findNum(list,num):
	list_new = [0,0]
	for n in range(len(list)-2):
		for t in range(1,len(list)-1):
			if list[n] + list[t] == num:
				list_new[1] = n
				list_new[0] = t
	return list_new		
	
'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

num = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","4",".",".","7","9"]
]
'''
def jude(num):
	sig = True
	text = []
	for n in num:
		for i in range(1,10):
			if n.count(str(i)) > 1:
				sig = False
	
	for i in range(9):
		for u in num:
			text.append(u[i])
		for h in range(1,10):
			if text.count(str(h)) > 1:
				sig = False	
				print(text)
		text.clear()
	
	for a in range(0,7,3):
		for b in range(0,7,3):
			for i in range(0+a,3+a):
				for n in range(0+b,3+b):
					text.append(num[i][n])
			for d in range(1,10):
				if text.count(str(d)) > 1:
					sig = False	
			text.clear()			
	return sig	
'''	
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]	

num = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
'''
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
 









	






