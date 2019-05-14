# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
# 三、对第四次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，可以手动结束游戏，
# 手动结束游戏后，打印本次游戏的胜率（胜利的把数除以玩的总把数）
# 提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）

import random

count = 0
win_count = 0
while True:
    print('''
-------石头剪刀布游戏开始-----  
请按照下面提示出拳：
石头【1】，剪刀【2】，布【3】，结束游戏【0】
''')
    x = int(input('请输入你的选项：'))
    y = random.randint(1,3)

    if (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        print('你输了,请继续')
    elif x == y:
        print('平局，请继续')
    elif x==0:
        print('下面是本次游戏你的胜率')
        break
    else:
        print('你赢了，请继续')
        win_count +=1
    count +=1
print('\n你的胜率是：','%.2f%%' % (win_count/count * 100))

