'''#什么是列表
ball = ['basketball','football','ppball','bigball','littleball']
message = "I like play "+ball[1].title()+"."
print(ball[0])
print(ball[-1])
print(message)

print("====================华丽的分割线=======================")

#修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'               #修改元素
print(motorcycles)

motorcycles.append('fenghuang')         #方法 append() 将元素 'ducati' 添加到了列表末尾，而不影响列表中的其他所有元素
print(motorcycles)

motorcycles.insert(1,'baoma')           #使用方法 insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值
print(motorcycles)

del motorcycles[1]                      #如果知道要删除的元素在列表中的位置，可使用 del 语句;使用 del 语句将值从列表中删除后，你就无法再访问它了
print(motorcycles)

popped_motorcycles = motorcycles.pop(2) #方法 pop() 可删除列表中的元素，并让你能够接着使用它（不填写索引默认弹出列表末尾的元素）。术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素
print(motorcycles)
print(popped_motorcycles)

remove_motorcycles = 'fenghuang'        #使用 remove() 从列表中删除元素时，也可接着使用它的值;方法 remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
motorcycles.remove(remove_motorcycles)
print(motorcycles)
print("I like ride "+remove_motorcycles)

print("==========================华丽的分割线===========================")

myfriend = ['刘德华','林青霞','泰勒斯威夫特','滨崎步','蕾哈娜','特朗普']
myfriend.sort()
print("I'd like to invite my friend",myfriend[2],myfriend[3],myfriend[4],"to my party")


cars = ['bmw','audi','toyota','subaru']
for car in cars:
    print(car+'是很好的汽车'+"\n")
print('但是我还是喜欢bmw')

list_value = []
for value in range(1,9):
    list_value.append(value**2)
print(list_value)


print("==========================华丽的分割线===========================")'''
#列表解析范例

#列出1~10
number_value = [squre**2 for squre in range(1,11)]
print(number_value)

#列出1~10中大于等于4的数字的平方
number_value = [squre**2 for squre in range(1,11) if squre>=4]
print(number_value)

# #实现两个列表中的元素逐一配对
# num1 = ['x','y','z']
# num2 = [1,2,3]
# num3 = [(a,b) for a in num1 for b in num2]
# print(num3)


print('\n'.join([''.join(['%s*%s=%-2s '%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


print(sum([sum2 for sum2 in range(1,1000001)]))

jishu_list = []
for jishu in range(1,11):
    if jishu%2!=0:
        print(jishu_list.append(jishu))



#创建切片














