#Author:Leva
class1 = {
    "math_teacher":"张老师",
    "stu1":"张三",
    "stu2":"李四",
    "stu3":"王五"
}
print(class1["math_teacher"])
for people,name in class1.items():
    print("\nPeople："+people)
    print("Name："+name)



user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key,value in user_0.items():
    print("\nKey："+key)
    print("Value："+value)