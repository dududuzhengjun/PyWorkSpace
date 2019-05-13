# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
# 1、输出指定格式的日期，提示：使用datetime模块
'''
import time
print('当前时间戳：',time.time())
    #当前时间戳： 1529908783.3990765
print('获取当前本地时间：',time.localtime())
    #获取当前本地时间： time.struct_time(tm_year=2018, tm_mon=6, tm_mday=25, tm_hour=14, tm_min=39, tm_sec=43, tm_wday=0, tm_yday=176, tm_isdst=0)
print('格式化可读时间模式：',time.asctime())
    #格式化可读时间模式： Mon Jun 25 14:39:43 2018
print('格式化日期：',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    #格式化日期： 2018-06-25 14:39:43

# 第二种方法
import datetime
print('当前年月日：',datetime.date.today())
    #当前年月日： 2018-06-25
print('格式化日期：',datetime.date.today().strftime('%Y/%m/%d'))
    #格式化日期： 2018/06/25
print(datetime.date(1941,1,5))
    #1941-01-05
'''
# 2、输出一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
'''
# 第一种方法
tmpStr = input('请输入字符串：')
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in tmpStr:
    if i.isalpha():
        alphaNum +=1
    elif i.isnumeric():
        numbers +=1
    elif i.isspace():
        spaceNum +=1
    else:
        otherNum +=1
print('字母/中文=%d'%alphaNum)
print('数字=%d'%numbers)
print('空格=%d'%spaceNum)
print('其他=%d'%otherNum)

# 第二种方法：使用正则表达式 re.findall()
import re
s = input('请输入一串字符：')
char=re.findall(r'[a-zA-Z]',s)#以列表类型返回全部能匹配的子串
num=re.findall(r'[0-9]',s)
blank=re.findall(r' ',s)
chi=re.findall(r'[\u4E00-\u9FFF]',s)#汉字的Unicode编码范围
other = len(s)-len(char)-len(num)-len(blank)-len(chi)
print('字母',len(char),'\n数字',len(num),'\n空格',len(blank),'\n中文',len(chi),'\n其他',other)
'''
# 3、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加通过键盘控制
'''
def main():
    basis = int(input("Input the basis number: "))
    n = int(input('Input the longest length of number: '))
    arr =[0]*n#定义一个长度为n，初值全部为0的一维数组。
    b = basis#通项
    sum = 0
    for i in range(n):
        arr[i] = basis
        sum += basis
        basis = basis * 10 + b
    print("%d="%sum, end ='')
    for i in range(n):
        print("%d"%arr[i],end = '')
        if i < n-1:
            print("+",end = '')
if __name__=='__main__':
    main()
'''
# 4、Python 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
for i in range(1, 1000):
    sum = 0
    for factor in range(1, i):
        if i % factor == 0:
            sum = sum + factor
    if i == sum:
        print(i)