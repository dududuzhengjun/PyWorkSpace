# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@create_time:2019-05-15 22:56
@detail:
@else: Don't stop learning!!!
"""
# 1、利用递归函数调用方式，将所输入的5个字符，以相反顺序显示出来。

# 2、有5个人坐在一起，问第5个人多少岁，他说比第4个人大2岁。问第4个人的岁数，
# 他说比第3个人大2岁。问第3个人的岁数，他说比第2人大2岁。问第2个人的岁数，他说比第1个人大2岁。
# 最后问第1个人，他说是10岁。请问第5个人多大岁数?


"""
# 3、给一个不多于5位的正整数，要求: a)求它是几位数，b)逆序显示各位数字。
num = input("请输入一个不多于5位的正整数：")
while 0<len(num)<6:
    print("你输入的是{}位数，逆序显示这个数字为{}".format(len(num),num[::-1]))
    break
else:print("你输入的不是不多于5位的正整数")

# 4、对于一个5位数，判断它是不是回文数。如12321 是回文数，个位与万位相同，十位与千位相同。
num = input("请输入一个五位数：")
while len(num)==5:
    reverse_num =num[::-1]
    if num==reverse_num:
        print("{}是回文数".format(num))
        break
    else:print(num,"不是回文数")
    break
else:print("你输入的不是五位数")
"""