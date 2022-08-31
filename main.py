# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

a = 65
a = int(input("请输入成绩:"))
print("成绩：%d" % a)
if a > 80:
    print("成绩优秀")
elif a > 60:
    print("成绩及格")
else:
    print("成绩不合格")

a = 65
a = int(input("请输入年纪:"))
print("年纪：%d" % a)
b = 1
if a >= 18 or b == 0:
    print("干活")
elif a > 40:
    print("休息")
else:
    print("养着")
