# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@create_time:2019-05-13 14:59
@detail:
@else: Don't stop learning!!!
"""

"""
# 1、'''输出如下图案（菱形）
      *
    ***
  *****
*******
  *****
    ***
      *
'''
nu = 1  # 开始值
k = 2   # 变量值
while nu >= 0:
    print(int((7 - nu) / 2) * '  ' + '*' * nu)
    nu += k
    if nu == 7:
        k = -k
"""

# 2、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13，...求出这个数列的前20项之和。
"""
a = 2
b = 1
sum = 0
for i in range(20):
    sum = a / b + sum
    a, b = (a + b), a
print(sum)

# 后一个分数的分子 = 前一个分数的分子 + 分母，后一个分数的分母 = 前一个分数的分子，循环个20次就有结果。注意，假设分子为a，分母为b，虽然
# a = a + b，
# 但此时a已经变成a + b了，所以再给b重新赋值的时候，得是(a + b) - b才能等于原分母b，所以重新赋值时就得写成a - b

# 方法一
from fractions import Fraction

def fibonacci(n):
    a, b = 1, 2
    res = [1]
    i = 1
    while i < n:
        a, b = b, a + b
        res.append(a)
        i += 1
    else:
        return res


result = fibonacci(21)

sum_result = sum([Fraction(i[0], i[1]) for i in zip(result[1:], result[0:-1])])
print(sum_result)

# 方法二
from fractions import Fraction

sum = 0
a, b = 2, 1
for i in range(20):
    sum = sum + Fraction(a / b)
    a = a + b
    b = a - b
print(sum)

# 方法三
sum = 0
a, b = 2, 1
for i in range(20):
    sum = sum + a / b
    a = a + b
    b = a - b
print(sum)
"""

# 3、求1+2!+3!+......20!的和。
"""
# 第一种方法
def recursion(n):  # '定义递归函数实现求阶乘功能'
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)
list = []  # 定义一个空的列表，将调用递归函数生成的阶乘值追加到列表
for i in range(1, 21):
    list.append(recursion(i))  # 将调用递归函数生成的阶乘值追加到列表
print(sum(list))  # 列表求和
Sum = 0
for i in range(1, 21):
    Sum += recursion(i)
print(Sum)
# 第二种方法
import math
Sum=0
num = int(input('请输入一个数字：'))
for i in range(1,num+1):
    F=math.factorial(i)
    Sum +=F
print('阶乘之和：',Sum)

# 第三种方法
Sum=0
factorial=1
num = int(input('请输入一个数字：'))
for i in range(1,num+1):
    factorial = factorial*i
    Sum +=factorial
print('阶乘之和：',Sum) 
"""
# 4、利用递归方法求5!的值
