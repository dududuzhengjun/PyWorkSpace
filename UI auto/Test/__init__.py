'''Author = Leva DU'''
def inp():
    x=input('请输入成绩：')
    try:
        float(x)
    except ValueError:
        pass
    else:
        return float(x)

def grade(x):
    try:
        if 60<x<80:
            print('良')
        elif 80<=x<=100:
            print('优秀')
        else:print('不及格')
    except TypeError:
        print('输入的不是数字')
grade(inp())