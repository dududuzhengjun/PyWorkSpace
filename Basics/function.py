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