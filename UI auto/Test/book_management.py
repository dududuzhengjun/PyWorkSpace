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

user_msg = {'admin':'123456','Jack':'654321'}
print('''
##################
欢迎访问图书管理系统
##################
''')
username = input('请输入用户名：')
password = input('请输入密码：')
book_list = [{'图书编号':'2','图书名称':'水浒传','图书位置':'403'},
             {'图书编号':'5','图书名称':'西游记后传','图书位置':'205'},
             {'图书编号':'6','图书名称':'三国演义','图书位置':'789'}]
def newBook():
    """新增图书"""
    dict_1 = {}
    book_list.append(dict_1)
    book_num = input('请输入图书编号：')
    dict_1['图书编号'] = book_num
    book_name = input('请输入图书名称：')
    dict_1['图书名称'] = book_name
    book_location = input('请输入图书位置：')
    dict_1['图书位置'] = book_location
    print(book_list)
def queryBook():
    """查询图书"""
    query_bookname = input('请输入要查询的图书名称：')
    for dict_name in book_list:
        if query_bookname == dict_name.get('图书名称'):
            print(book_list[book_list.index(dict_name)])
            break
    else:
        print('\n你查询的图书不存在')
def delBook():
    """删除图书"""
    del_bookname = input('请输入要删除的图书名称：')
    for dict_name in book_list:
        if del_bookname == dict_name.get('图书名称'):
            book_list.remove(dict_name)
            print(book_list)
            break
    else:
        print('\n你删除的图书不存在')
def modifyBook():
    """修改图书"""
    modify_bookname = input('请输入要修改的图书名：')
    for dict_name in book_list:
        if modify_bookname == dict_name.get('图书名称'):
            book_num = input('请输入修改后的图书编号：')
            book_position = input('请输入修改后的图书位置：')
            book_list[book_list.index(dict_name)] = {'图书编号':book_num,'图书名称':modify_bookname,'图书位置':book_position}
            print(book_list)
            break
    else:
        print('\n你修改的图书不存在')

while True:
    if (username,password) in user_msg.items():
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
            newBook()
        elif option==2:
            queryBook()
        elif option==3:
            delBook()
        elif option==4:
            modifyBook()
        elif option==5:
            print('Bye')
            break
        else:
            print('请输入1~5之间的数字')
else:
    print('用户名或密码错误，请重新输入')
