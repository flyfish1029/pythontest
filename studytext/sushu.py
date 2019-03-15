#-*- coding:utf-8 -*-

from math import sqrt
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return n

#L = list(range(101))
#List = L[2:101]
def fn():
	return list(map(is_prime, list(range(1, 101))))
L2 = []
L2 = fn()
print(L2)