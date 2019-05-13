# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""


# 1、有4个数字：1、2、3、4，它们能组成多少个互不相同且无重复数字的3位数？各是多少？
'''
# 第一种方法
from itertools import permutations
num = 0
for i in range(1,5):
    for j in range (1,5):
        for k in range(1,5):
            if (i != j)and ( j != k )and ( k != i):
                num+=1;
                print(i,j,k)
print ("total num is :%d" % num)

# 第二种方法
n = []
for i in permutations('1234',3):
    n.append(''.join(i))
print(n)
print('可组成{}个三位数'.format(len(n)))
'''

# 2、一个整数加上100后是一个完全平方数，再加上168后又是一个完全平方数，请问该数是多少？
'''
import math
# 第一种方法
for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))

    if(x * x == i + 100) and (y * y == i + 268):

            print('Maybe the number is :',i)
exit()

# 第二种方法
n = 0
while (n+1)**2-n*n<=168 :
    n+=1

for i in range((n+1)**2):
    if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5) and i-100>0:
        print('可能存在的数是：',i-100)
'''