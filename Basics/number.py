import this
#1、整数
a = 1+1
b = 1-1
c = 1*1
d = 1/1
e = 2**2
f = (a+b)*e
print(a,b,c,d,e,f)

#2、浮点数
g = 0.2+0.1
print(g)

#3、使用函数str()避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#Python2中的整数
'''在Python 2中，整数除法的结果只包含整数部分，小数部
分被删除。请注意，计算整数结果时，采取的方式不是四舍五入，而是将小数部分直接删除。
在Python 2中，若要避免这种情况，务必确保至少有一个操作数为浮点数，这样结果也将为
浮点数'''


