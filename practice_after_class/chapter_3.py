# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""


# 1、输入某年某月某日，判断这一天是这一年的第几天？
'''
# 思路：先判断是否为闰年，这关系到 2 月份的天数。
# 之后再根据月份值把前几个月的天数累积加起来，最后再加上个“日”，就可以了

# 第一种方法
dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])  #获取年份
m = int(dat[5:7])  #获取月份
d = int(dat[8:])  #获取日

ly = False

if y%100 == 0:  #若年份能被100整除
    if y%400 == 0:  #且能被400整除
        ly = True  #则是闰年
    else:
        ly = False
elif y%4 == 0:  #其它情况下，若能被4整除
    ly = True  #则为闰年
else:
    ly = False

if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
    if i == m:
        for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
            days += ms[j]
        print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案


# 第二种方法
import datetime

y = int(input('请输入4位数字的年份：'))  #获取年份
m = int(input('请输入月份：'))  #获取月份
d = int(input('请输入是哪一天：'))  #获取“日”

targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
print(targetDay - datetime.date(targetDay.year-1, 12, 31))  #减去上一年最后一天，可得解

# 第三种方法
import datetime

y = int(input('请输入4位数字的年份：'))  #获取年份
m = int(input('请输入月份：'))  #获取月份
d = int(input('请输入是哪一天：'))  #获取“日”

targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
print('%s是%s年的第%s天。'% (targetDay, y, dayCount.days))

# 第四种方法
import datetime
from pip._vendor.distlib.compat import raw_input

dtime = raw_input("请输入求天数的日期(20161115)：")
tnum = datetime.datetime.strptime(dtime,'%Y%m%d').strftime("%j")
print (dtime + "在一年中的天数是: " + tnum + "天。")
'''

# 2、输入3个整数x、y、z，请把这3个数有小到大输出
'''
# 第一种方法
x = input("请输入第一个整数：")
y = input("请输入第二个整数：")
z = input("请输入第三个整数：")
i = [x,y,z]
i.sort()
print(i)

# 第二种方法
import re

x, y, z = re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
x, y, z = int(x), int(y), int(z)

max_num = max(x, y, z)
min_num = min(x, y, z)
print(min_num, x+y+z-min_num-max_num, max_num)

# 第三种方法
# 用 re.split() 得到 3 个字符型数字的列表，把字符转换为数字，排下序，然后 print() 代码如下：
import re

lst = re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst.sort()
print(lst)
'''

# 3、输出99乘法表
'''
# 第一种方法（一）
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (j,i,i*j),end=" ")
    print()

# 第一种方法（二）（格式化整数方式不同）
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

# 第二种方法
print('\n'.join([''.join(['%s*%s=%-2s '%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
'''