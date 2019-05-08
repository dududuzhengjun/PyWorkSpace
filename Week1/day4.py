'''Author = Leva DU'''
'''_username = input("请输入用户名:")
_password = input("请输入密码:")

username = "admin"
password = "admin123"

if _username==username and _password==password:
    print("Welcome user {name} login Python".format(name=username))
else:
    print("Invalid username or password")

print(id(username))'''


count = 0
while count<3:
    my_age = int(input("猜我的年龄："))
    if not my_age.isdigit():
        print("你输入的不是整数，请重新输入~")
    else:
        if my_age<10:
            print("我有那么小吗？哈哈哈哈哈")
        elif my_age>=10 and my_age<24:
            print("再猜猜，很接近啦~微笑")
        elif my_age>24:
            print("你才那么老呢，哼╭(╯^╰)╮")
        else:
            print("对啦，you get it！！！")
            break
        count +=1
else:
    print("You have tried too many times..next time..bye~~~~~")