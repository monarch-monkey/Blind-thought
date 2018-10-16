'''
编写一个函数，其作用是将输入的字符串反转过来


str = 'welcome to my world,hi'
'''
def reverseStr(str):
	str_list = []
	for i in str:
		str_list.append(i)
	str = ''
	str_list.reverse()
	for s in str_list:
		str += s
	return 	str	


#给定一个 32 位有符号整数，将整数中的数字进行反转。

num = -123
#调用了上面的函数reverseStr，作用是将输入的字符串反转过来
def reverseNum(num):
	if num == 0:
		return 0
	if num > 0:
		return int(reverseStr(str(num)))
	if num < 0:
		num = -num
		return -int(reverseStr(str(num)))		

#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#str = "zzbbbbx"
def notRepet(str):
	sig = -1
	for n in range(len(str)):
		if str.count(str[n]) == 1:
			sig = n
			break
	return sig 
	
'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true

s = "anagram"
t = "nagaram"
'''
def isSame(s,t):
	sig = False
	s1 = list(s)
	s1.sort()
	t1 = list(t)
	t1.sort()
	if s1 == t1:
		sig = True
	else:
		sig = False
	return sig

	
	'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true		
'''
import string

def func(str):
	temp = []
	sig = True
	#数据清洗
	str_new = str.lower()
	for i in str_new:
		if i not in string.punctuation:
			temp.append(i)
	for a in temp:
		if ' ' in temp:           #必须这样处理，不然会清洗不干净
			temp.remove(' ')
	str_new = ''.join(temp)
	#判断回文规则
	for a in range(len(temp)//2):
		if temp[a] != temp[-a-1]:
			sig = False
			break
	return sig
	
'''
实现 atoi，将字符串转为整数。
该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，
这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
若函数不能执行有效的转换，返回 0。
说明：
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

str = "    -78742"
'''
def push_num(str):
	sig = 0
	max = 'INT_MAX (2**31−1)' 
	min = 'INT_MIN (−2**31)' 
	if str == '' or str.isspace():   #判断是否是空字符串或者只包含空白字符
		return sig 
			
	temp = []
	for i in str:
		temp.append(i)
	for a in range(len(temp)):
		if temp[0] == ' ':           #牢记循环内多列表内容修改，列表长度会发生变化
			temp.remove(temp[0])
	
	if temp[0] == '-' or temp[0].isnumeric():                #判断是否首位是'-'或者数字
		sig = int(''.join(temp))
		
	if sig < -(2**31):
		return  min
	if sig > (2**31)-1:
		return max   
	return sig

	'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 
(从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2		
'''

def findneedle(haystack,needle):
	
	sig = -1
	if needle == '':
		sig = 0
	elif len(haystack) == 1:
		if needle == haystack:
			sig = 0
	elif len(haystack) < len(needle):
		return sig
	elif len(needle) == 1:
		for i in range(len(haystack)):
			if haystack[i] == needle:
				sig = 0
	else:
		for i in range(len(haystack)):
			if haystack[i-1:i+len(needle)-1] == needle:		
				sig = i-1
				break
	return sig	

	'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
'''


'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:['cc','c']

输入: ["flower","flow","flight"]
输出: "fl"
'''
def same_str(list):
	'''
	这是一个查找字符串数组中的最长公共前缀的函数
	:type strs: List[str]
    :rtype: str
	'''
	a = []
	target = ''
	
	#特殊情况处理
	if len(list) == 1:
		return list[0]
	elif list == []:
		return target
	#找出最短值，防止索引溢出
	for i in list:
		a.append(len(i))
	temp_str = list.pop(a.index(min(a)))
	#比对数据
	for t in range(len(temp_str)):		
		for l in list:
			if temp_str[t] != l[t]:
				return temp_str[0:t]
	#完整完成循环后，将temp_str赋值返回
	target = temp_str				
	return target			
print(same_str(list))	

















  














	

	
	
	
	
	
	
	
	
	
	
	



















