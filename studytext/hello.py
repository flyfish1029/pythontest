#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#h = input('height: ')
#w = input('weight: ')
height = 1.75
weight = 77

bmi = weight/(height*height)
if bmi < 18.5:
	print('过轻')
elif bmi >= 18.5 and bmi < 25:
	print('正常')
elif bmi >= 25 and bmi < 28:
	print('过重')
elif bmi >= 28 and bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')