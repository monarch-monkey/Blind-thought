import re

def str_seq(str):

	a = re.split('(\w+)',str)
	a.reverse()
	str_new = ''.join(a)
	return str_new

input_str = 'hi,welcome to beijing.'
print(str_seq(input_str))



