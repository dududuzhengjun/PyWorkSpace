'''Author = Leva DU'''
import getpass

username = input("请输入用户名：")
password = input("请输入密码：")
print(type(password))
salary = int(input("请输入薪资："))

info ='''
-------info of %s -----  
姓名：%s
密码：%s
薪资：%d
'''%(username,username,password,salary)
print(info)

info2 ='''
-------info2 of {_username} -----  
姓名：{_username}
密码：{_password}
薪资：{_salary}
'''.format(_username=username,
           _password=password,
           _salary=salary)
print(info2)

info3 ='''
-------info3 of {0} -----  
姓名：{0}
密码：{1}
薪资：{2}
'''.format(username,password,salary)
print(info3)
