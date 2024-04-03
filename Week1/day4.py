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


count = 0  # 初始化猜测次数为0

while count < 3:  # 当猜测次数小于3时执行循环
    input_age = input("猜我的年龄：")  # 提示用户输入年龄
    if not input_age.isdigit():  # 检查输入是否为数字字符串
        print("你输入的不是整数，请重新输入~")  # 如果输入不是数字字符串，输出提示信息
    else:
        my_age = int(input_age)  # 将输入的年龄转换为整数
        if my_age < 10:
            print("我有那么小吗？哈哈哈哈哈")  # 年龄小于10的情况
        elif my_age >= 10 and my_age < 24:
            print("再猜猜，很接近啦~微笑")  # 年龄在10到24之间的情况
        elif my_age > 24:
            print("你才那么老呢，哼╭(╯^╰)╮")  # 年龄大于24的情况
        else:
            print("对啦，you get it！！！")  # 年龄猜对的情况，跳出循环
            break

        count += 1  # 每次循环结束后，猜测次数加1
else:
    print("You have tried too many times..next time..bye~~~~~")  # 循环结束时猜测次数仍小于3，输出提示信息count = 0  # 初始化猜测次数为0

while count < 3:  # 当猜测次数小于3时执行循环
    input_age = input("猜我的年龄：")  # 提示用户输入年龄
    if not input_age.isdigit():  # 检查输入是否为数字字符串
        print("你输入的不是整数，请重新输入~")  # 如果输入不是数字字符串，输出提示信息
    else:
        my_age = int(input_age)  # 将输入的年龄转换为整数
        if my_age < 10:
            print("我有那么小吗？哈哈哈哈哈")  # 年龄小于10的情况
        elif my_age >= 10 and my_age < 24:
            print("再猜猜，很接近啦~微笑")  # 年龄在10到24之间的情况
        elif my_age > 24:
            print("你才那么老呢，哼╭(╯^╰)╮")  # 年龄大于24的情况
        else:
            print("对啦，you get it！！！")  # 年龄猜对的情况，跳出循环
            break

        count += 1  # 每次循环结束后，猜测次数加1
else:
    print("You have tried too many times..next time..bye~~~~~")  # 循环结束时猜测次数仍小于3，输出提示信息