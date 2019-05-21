# -*- coding:utf-8 -*- 
"""
@project: PythonStudy
@filename：file_util
@Author: duzhengjun
@create_time：2019-05-18 23:04
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
# data = open('yesterday',encoding='utf-8').read()

f = open('yesterday','r')   #文件句柄
# data1 = f.write('goodboy')
# data = f.read()
# for i in f.readlines()[4:11]:
#     print(i)

print(f.read(100))
