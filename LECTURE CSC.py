Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def count_digits(s):
	count = 0
	for digit in s:
		if digit.isdigit():
			count +=1
	return count

>>> count_digits('xxsnfks2223xx')
4
>>> t = (1,2,3)
>>> type(t)
<class 'tuple'>
>>> t[-1]
3
>>> t[0]
1
>>> t[1:2]
(2,)
>>> t
(1, 2, 3)
>>> t[0] = 99
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t[0] = 99
TypeError: 'tuple' object does not support item assignment
>>> t.index(1)
0
>>> t.index(4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t.index(4)
ValueError: tuple.index(x): x not in tuple
>>> t.index(2)
1
>>> t.count(2)
1
>>> for item in t:
	print (item)

	
1
2
3
>>> lst = [[1,2,3], [4,5,6], [7,8,9], [99,0,0]]
>>> lst[0]
[1, 2, 3]
>>> lst[3][0]
99
>>> len(lst)
4
>>> len(lst[0])
3
>>> lst = [[1,1], [2,3,4]]
>>> sum = 0
>>> for i in range (len(lst)):
	for j in range (len(lst[0]))
	
SyntaxError: invalid syntax
>>> lst = [[1,1], [2,3,4]]
>>> sum = 0
>>> for i in range (len(lst))
SyntaxError: invalid syntax
>>> for i in range (len(lst)):
	for j in range (len(lst[0])):
		sum = sum + lst[i][j]
	print (sum)

	
2
7
>>> range(2)
range(0, 2)
>>> list(range(0,2))
[0, 1]
>>> list(range(0,5))
[0, 1, 2, 3, 4]
>>> list(range(2,5))
[2, 3, 4]
>>> lst = [[2,3,4] , [1,1]]
>>> lst[0][0]
2
>>> lst[0][1]
3
>>> lst[0][2]
4
>>> lst[0][3]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lst[0][3]
IndexError: list index out of range
>>> def is_ok (group_list, class_list):
	''' return true if every student in class_list is in group_list'''
	ok = True
	for student in class_list:
		total_groups = 0
		for sublist in group_list:
			if student in sublist:
				total_groups += 1
		if total_groups != 1:
			ok = False
	return ok

>>> is_ok ([],[])
True
>>> is_ok([1], [2])
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    is_ok([1], [2])
  File "<pyshell#60>", line 7, in is_ok
    if student in sublist:
TypeError: argument of type 'int' is not iterable
>>> 
