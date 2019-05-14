# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@create_time:2019-05-13 17:17
@detail:
@else: Don't stop learning!!!
"""
operation = {1: '添加图书', 2: '查询图书', 3: '删除图书', 4: '修改图书信息', 5: '退出'}
name_passwd = {'admin': '123456', 'jack': '654321'}
book_list = [['1', 'a', 'a1'], ['2', 'b', 'b2']]
name, passwd = input('输入用户名'), input('输入密码')
if (name, passwd) in list(name_passwd.items()):
    operate = int(input('请输入选项'))
    if operate == 1:
        book_num = input('请输入图书编号')
        book_name = input('请输入图书名称')
        book_position = input('请输入图书位置')
        new_book = [book_num, book_name, book_position]
        book_list.append(new_book)
    elif operate == 2:
        print('查询图书')
    elif operate == 3:
        book_name1 = input('请输入需要删除的图书名称')
        for i in book_list:
            if book_name1 in i:
                book_list.remove(i)
    elif operate == 4:
        print('修改图书信息')
    elif operate == 5:
        print('退出')
else:
    print('用户名或密码错误')

for i in book_list:
    print(i)

