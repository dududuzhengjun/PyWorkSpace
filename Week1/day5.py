'''Author = Leva DU'''
import random

secret = random.randint(0, 9)  # 这里使用random()产生0~9之间整数
# print(secret)
print('------猜数字游戏！-----')
guess = -1
N = 0  # 记录次数
while guess != secret:
    temp = input('请输入数字0--9之间：\n')
    if not temp.isdigit():  # 判断输入的是否为非整数
        print('输入内容必须为整数！！！！\n再来一次吧\n')
    else:
        N += 1
        guess = int(temp)
        if guess > secret:
            print('遗憾，太大了！\n')
        if guess < secret:
            print('遗憾，太小了！\n')
if guess == secret:
    print('预测{}次，你猜中了！'.format(N))