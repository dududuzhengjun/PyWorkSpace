#Author:Leva
import time,math
# week=['礼拜一','礼拜二','礼拜三','礼拜四','礼拜五','礼拜六','礼拜日']
# number=int(input('请输入1-7的整数：'))
# print('今天是'+week[number-1])

#向li2中插入元素
li2=[1,2,3,4,5]
li2.insert(0,0)
li2.insert(5,66)
li2.insert(7,11)
li2.insert(8,22)
li2.insert(9,33)
print(li2)
#对li2进行永久性排序（升序）
li2.sort()
print(li2)
'''删除列表元素的方法
1、pop()直接删除列表末尾元素
2、pop(index)知道元素索引，通过索引删除列表元素
3、remove()根据元素值删除列表中的元素
4、del 列表名称[索引值] （补充）
'''

tu = (1,2,3)
tu2 = (4,5,6)
print(3 in tu2)




for i in range(1,10):
        for j in range(1,i+1):
            print('{}*{}={}\t'.format(j,i,i*j),end='')
        print()

def test():
    print("hello")
test()





