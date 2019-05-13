# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
# 1、输出所有的“水仙花数”，所谓的“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1*1*1+5*5*5+3*3*3
'''
# 第一种方法
for a in range(1,10):  #  从1开始, 百位不能为0
     for b in range(10):  #  从0开始, 十位可以为0
         for c in range(10):  #  从0开始, 个位也可以为0
             s1= a*100+b*10+c  #  三位数=百位+十位+个位
             s2= pow(a,3)+pow(b,3)+pow(c,3) #  每个位置的数的n次方之和
             if s1==s2:
                 print(s1, "是水仙花数")

# 第二种方法
for i in range(100,1000):
     s = str(i)
     if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
         print(s, "是水仙花数")
'''
# 2、对于一个正整数分解质因数。例如：输入90，输出90=2*3*3*5
'''
# 第一种方法
while 1:
    n = int(input('请输入一个整数：'))
    print('%d='%n,end='')
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                if n==1:
                    print('%d'%i,end='')
                else:
                    print('%d*'%i,end='')
                break
    print()

# 第二种方法
from math import sqrt
while 1:
    n=int(input('请输入整数：'))
    print ("%d = " %n , end = '')
    while 1:
        for i in range(2,int(sqrt(n)+1)):
            if n%i==0:
                print('%d*'%i,end='')
                n=int(n/i)
                break
        else:
            print(n)
            break

# 第三种方法
def prime(n):
    L=[ ]
    while n>1:
        for i in range(2,n+1):
            if n % i ==0:
                n = int(n/i)
                L.append(i)
                break
    return L
while 1:
    s = input('请输入一个正整数：')
    if s.isdigit() and int(s)>0:
        print(s,'=','*'.join([str(x) for x in prime(int(s))]))#*.join(sequence)用*号连接元素序列
    else:
        print('请输入一个正整数：')
'''
# 3、输出第10个斐波那契数列。斐波那契数列，又称黄金分割数列，指的是这样一个数列：0，1，1，2，3，5，8，13，21，34....
'''
# 第一种方法
nterms = int(input("你需要几项？"))
# 第一和第二项
n1 = 0
n2 = 1
count = 2
# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,",",n2,end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth,end=" , ")
       # 更新值
        n1 = n2
        n2 = nth
        count += 1

# 第二种方法
a=0
b=1
print(a)
print(b)
i=1
while i<9:
 c=a+b
 print(c)
 a=b
 b=c
 i+=1
'''
# 4、利用条件运算符的嵌套来完成此题：高于90分的学习成绩用A表示，60分到89分之间的学习成绩用B表示，60分以下的学习成绩用C表示
score = input("请输入成绩：")
score = float(score)
if score >= 90:
    print("成绩为:%s" % ("A"))
elif score >= 60:  # 在这种情况下，二者等效score >= 60 and score < 89
    print("成绩为:%s" % ("B"))
else:
    print("成绩为:%s" % ("C"))
