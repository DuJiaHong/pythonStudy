# if--else练习，计算BMI体脂
# 计算公式为：BMI=体重（kg）/ 身高（m）²，体重正常：18.5-24.9，超重：25-29.9，一级肥胖：30-34.9。
def bmiCount():
    weight = float(input("请输入体重（KG）："))
    height = float(input("请输入身高（M）："))
    bmi = weight / (height * height)
    print("你的身高：%.2f,你的体重%.2f,BMI指数%.2f" % (height, weight, bmi))

    if bmi >= 35:
        print("超胖")
    elif 30 <= bmi < 35:
        print("肥胖")
    elif 25 <= bmi < 30:
        print("过重")
    elif 18.5 <= bmi < 25:
        print("适中")
    else:
        print("过轻")


if __name__ == '__main__':
    bmiCount()
