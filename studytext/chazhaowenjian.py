#-*- coding:utf-8 -*-

__author__='xiewei'

import os

def find_file(kw, path):
	file_list = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and kw in x]
	for x in file_list:
		print('文件名: %s \t 路径:%s' % (x, os.path.relpath(path)))
	dir_list = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
	for x in dir_list:
		sub_path = os.path.join(path, x)
		find_file(kw, sub_path)


if __name__ == '__main__':
	keyword = input('please input the keyword:')
	current_path = os.path.abspath('.')
	find_file(keyword, current_path)