'''用引号引起来的都是字符串，无论单双引号'''

#1、使用方法修改字符串中的大小写
name = "leva du"
print(name.title())  #title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
print(name.upper())  #upper() 以大写字母的方式显示每个单词
print(name.lower())  #upper() 以小写字母的方式显示每个单词

#2、合并（拼接）字符串
first_name = "Leva"
last_name = "Du"
full_name = first_name +" "+ last_name
print("Hello,"+full_name.title()+"!")

#3、使用制表符或换行符来添加空白
print("\tPython")  #制表符：\t
print("Languages:\nPython\nC\nJavaScript")  #换行符：\n
print("Languages:\n\tPython\n\tC\n\tJavaScript")  #同一个字符串中同时包含制表符和换行符

#4、删除空白
favorite_language = " Python "
print(favorite_language.rstrip())  #剔除末尾空白
print(favorite_language.lstrip())  #剔除开头空白
print(favorite_language.strip())   #剔除两端空白，这种删除只是暂时的，接下来再次询问favorite_language的值时，依旧包含多余的空白

my_favorite_language = " Albert Einstein once said, 'A person who never made a mistake never tried anything new.' "
print(my_favorite_language.lstrip())



