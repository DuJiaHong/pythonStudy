class human(object):
    """
    类学习
    """

    def hm_sport(self):
        print("正在锻炼")

    def hm_study(self):
        print("正在学习")

    def hm_sleep(self):
        print("正在休息")

    def hm_work(self):
        print("正在工作")

    def __init__(self, name, age, sex, height, weight, qualification):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self._weight = weight
        self.qualification = qualification

    def human_bmi(self):
        bmi = self._weight / (self.height * self.height)
        print("你的身高：%.2f,你的体重%.2f,BMI指数%.2f" % (self.height, self._weight, bmi))

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


class xiaohong(human):
    def __init__(self, name, age, sex, height, weight, qualification):
        super().__init__(name, age, sex, height, weight, qualification)


if __name__ == "__main__":
    dagou = human("大狗", 20, "boy", 1.77, 70, 1)
    dagou._weight = 88
    print(dagou._weight)
    dagou.human_bmi()

    xiaohong = xiaohong("大狗", 20, "boy", 1.88, 50, 1)
    xiaohong.human_bmi()
    # dagou.run()
