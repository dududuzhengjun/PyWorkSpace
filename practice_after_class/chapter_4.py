# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
# 1、暂停一秒输出，并格式化当前时间
'''
import datetime
import time
time.sleep(1)   # 暂停一秒输出
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()) ))  # 格式化时间

# ls =datetime.datetime.now()
# time.sleep(1)
# ls.strftime('%Y-%m-%d %H:%M:%S')
# print(ls)
'''

# 2、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
'''
month=input("请输入月份:")
if month.isdigit():
    month=int(month)
    a=0
    b=1
    for i in range(month-1):
        a,b=b,a+b
    print("%d月份以后兔子有%d对"%(month,b))
else:
    print("输入有误请重新输入")
'''

# 3、判断101~200之间有多少个素数，并输出所有素数
'''
# 第一种方法
b = 0
for a in range(101,201):
    k = 0
    for i in range(2,a):
        if a % i == 0 :
            k += 1
    if k == 0 :
        print(a)
        b +=1
print("素数一共有",b,"个")

# 第二种方法
n = 0
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,'是质数')
        n +=1
print("素数共有",n,"个")
'''