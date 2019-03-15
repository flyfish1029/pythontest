# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

chrome_driver = 'D:\学习文档\chromedriver.exe'
wd = webdriver.Chrome(executable_path=chrome_driver)
wd.get("http://www.renren.com")
wd.maximize_window()

try:
    """这段可以查看selenium的源码,属于smart wait"""
    email = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'email')),message=u'元素加载超时!')
    email.send_keys("15801088785")
    passwd = WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located((By.ID,'password')),message=u'元素加载超时!')
    passwd.send_keys("tiger@123")
    wd.find_element_by_id("login").click() #点击登录
except NoSuchElementException as e:
    print(e.message)
