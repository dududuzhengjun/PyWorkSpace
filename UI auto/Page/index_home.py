'''Author = Leva DU'''
from selenium import webdriver

driver = webdriver.Chrome()
print("正在启动谷歌浏览器")
driver.get("http://www.baidu.com")
