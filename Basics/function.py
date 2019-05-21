# -*- coding:utf-8 -*-
# @Author: Leva
"""
@project: PythonStudy
@time:
@detail:
@else: Don't stop learning!!!
"""
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')


def describe_city(city_name,city_country='China'):
    """显示城市的信息"""
    city_dict = {'城市名':city_name,'所属国家':city_country}
    return city_dict
japan = describe_city('东京','日本')
print(japan)

def greet_users(names):
    """向列表中的每一位用户都发出简单的问候"""
    for name in names:
        msg = "Hello,"+name.title()+'!'
        print(msg)
usernames = ['1','2','3']
greet_users(usernames)

magicians = ['张三','李四','王五','赵六']
def show_magicians():
    for name in magicians:
        print(name)

def make_great(magicians):
    n=len(magicians)
    for i in range(0,n):
        magicians[i]="The Great "+magicians[i]
    return magicians

show_magicians()
make_great(magicians)
show_magicians()


a = 0
def myfun():
    global a
    a+=1

myfun()
print(a)

























