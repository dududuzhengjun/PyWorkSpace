# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
# {'book_num':1,'book_name':'天龙八部','book_location':'c区3架'}
# 四、图书管理系统功能
#  完成图书管理系统：
#   输入正确的账号和密码能登录 不正确的不能  正确的用户名和密码为 admin和123456
#  Jack和654321

truename1,trueword1 = 'admin','123456'
truename2,trueword2 = 'Jack','654321'
print('''
##################
欢迎访问图书管理系统
##################
''')
username = input('请输入用户名：')
password = input('请输入密码：')
book_list = [{'图书编号':'2','图书名称':'3','图书位置':'4'},{'图书编号':'5','图书名称':'6','图书位置':'7'}]
if (username==truename1 and password==trueword1) or (username==truename2 and password==trueword2):
    print('''
    登录成功\n
    -----------欢迎进入图书管理系统------------
    【1】：添加图书
    【2】：查询图书
    【3】：删除图书
    【4】：修改图书信息
    【5】：退出
    ''')
    option = int(input('请输入您的选项：'))
    if option==1:
        dict_1 = {}
        book_list.append(dict_1)
        print('请输入图书编号：')
        book_num = input()
        dict_1['图书编号'] = book_num
        print('请输入图书名称：')
        book_name = input()
        dict_1['图书名称'] = book_name
        print('请输入图书位置：')
        book_location = input()
        dict_1['图书位置'] = book_location
        print(book_list)
    elif option==2:
        print('查询图书')
    elif option==3:
        del_bookname = input('请输入要删除的图书名称：')
        for dict_name in book_list:
            if del_bookname in dict_name.values() :
                book_list.remove(dict_name)
        print(book_list)
    elif option==4:
        print('修改图书信息')
    elif option==5:
        print('Bye')
    else:
        print('请输入1~5之间的数字')
        pass
else:print('用户名或密码错误，请重新输入')