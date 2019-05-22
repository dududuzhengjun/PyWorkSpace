# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@create_time:2019-05-15 23:00
@detail:
@else: Don't stop learning!!!
"""
# 1、请输入一周中某天的名称的第一个英文字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
def juge(num,week_list):

    w = input('请输入第%s个字母:'%num)
    w = w.lower()
    res = []
    state = 0
    for week in week_list:
        if w == week[0 + num - 1: 1 + num - 1]:
            state += 1
            res.append(week)

    if state == 1:
        print('是%s'% res[0])
    elif state > 1:
        print('还要输入一次')
        num += 1
        week_list = res
        juge(num, week_list)
    else:
        print('非法输入')


if __name__ == '__main__':
    #  初始条件
    num = 1
    week_list = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']
    juge(num, week_list)

# 2、按相反的顺序输出列表的值。

# 3、按逗号分隔列表。

# 4、练习函数调用。