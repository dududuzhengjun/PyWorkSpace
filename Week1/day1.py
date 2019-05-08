import getpass
import os

'''Linux中如果想要类似于执行shell脚本一样执行python脚本，例： ./hello.py ，那么就需要在 hello.py 文件的头部指定解释器，如下：'''
#!/usr/bin/env python  声明解释器,env显示当前用户的环境变量
#ps：执行前需给予 hello.py 执行权限，chmod 755 hello.py

print("Hello World")

'''变量：
    变量名只能是字母、数字或下划线的任意组合
    变量名的第一个字符不能是数字
    以下关键字不能声明为变量名
    ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 
'try', 'while', 'with', 'yield']'''
my_name = "Leva Du"
my_nickname = my_name
print("My name is "+my_nickname) #用+或者,都可以起到连接的作用
my_name = "DuZhengJun"
print(my_name+"和"+my_nickname)



names = ["a","b","c","d","e","f"]
'''取下标为0的元素'''
print(names[0])

'''取下标1至下标4之间的元素，包括1，不包括4'''
print(names[1:4])