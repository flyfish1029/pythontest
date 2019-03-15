#-*- coding:utf-8 -*-

__author__='xiewei'

from collections import Counter

c = Counter()
for ch in 'xiewei':
	c[ch] = c[ch] + 1

c
print(c)