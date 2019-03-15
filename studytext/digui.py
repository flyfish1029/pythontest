#-*- coding:utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	return fact(n - 1) + fact(n - 2)

n = int(input('n = '))
print(fact(n))