# -*- coding: utf-8 -*-
'''
@Project : PyWorkSpace
@File    : wan_web_ui_test.py
@Author  : duzhengjun
@Time    : 2023/2/10 22:16
@else    : Don't stop learning!!!
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def login_wanweb (url,username,password):
    # 指向驱动位置
    # 下载地址：https://chromedriver.storage.googleapis.com/index.html
    # path = Service('../venv/chromedriver.exe')
    # driver = webdriver.Chrome(service=path)

    # 打开链接
    driver = webdriver.Chrome()
    # 打开wan_web后台
    driver.get(url)
    time.sleep(3)

    print("正在启动谷歌浏览器")

    # 浏览器全屏
    driver.maximize_window()

    # 找到输入框，这里需要自行在F12的Elements中找输入框的位置，然后在这里写入
    user_input = driver.find_element(by=By.XPATH, value='//input[@placeholder=\"请输入用户名\"]')
    pw_input = driver.find_element(by=By.XPATH, value='//input[@placeholder=\"请输入密码\"]')
    login_btn = driver.find_element(by=By.XPATH, value='//button[@type=\"submit\"]')
    # 输入用户名和密码，点击登录
    user_input.send_keys(username)
    pw_input.send_keys(password)
    print("输入账号名和密码")
    time.sleep(1)
    login_btn.click()
    time.sleep(2)
    print("登录成功")
    application_btn = driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/section/section/main/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div')

    application_btn.click()

    return driver

# def application ():
#     # 实现wan_web申办业务
#     application_btn = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/section/section/main/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div')
#
#     application_btn.click()
#     return driver

if __name__ == '__main__':
    # 定义目标URL信息
    wan_web_url = {
        'url': 'https://200000001-zaixian.sdndc.cn/account/login',
        'username': '13002840927',
        'password': 'Dzj940927'
    }
    # 登录
    driver = login_wanweb(wan_web_url['url'], wan_web_url['username'], wan_web_url['password'])
    # driver = application()

