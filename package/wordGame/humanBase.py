import random


class humanBase(object):
    """
    类学习，实现文字养成类游戏
    """

    def hm_sport(self):
        if self.show_info:
            print("正在锻炼。。")
            print("时间过去了3个月")
            print("你的属性发生了变化")
        self.money = self.money - 150
        self.age = self.age + 0.25
        self.qualification = self.qualification + random.uniform(0, 0.2)
        if self.age <= 18:
            self.height = self.height + random.uniform(0.008, 0.018)  # girl
        self.weight = self.weight - random.uniform(0.2, 0.4)
        # self.height = self.height + random.uniform(0.012,0.024) # boy

    def hm_study(self):
        if self.show_info:
            print("正在学习")
            print("时间过去了3个月")
            print("你的属性发生了变化")
        self.money = self.money - 200
        self.age = self.age + 0.25
        if self.age <= 18:
            self.qualification = self.qualification + random.uniform(0.2, 0.5)
            self.height = self.height + random.uniform(0.003, 0.008)  # girl
            self.weight = self.weight + random.uniform(0.7, 1)
        else:
            self.weight = self.weight + random.uniform(0, 0.3)
            self.qualification = self.qualification + random.uniform(0.1, 0.3)

    def hm_sleep(self):
        if self.show_info:
            print("正在休息")
            print("时间过去了3个月")
            print("你的属性发生了变化")
        self.money = self.money - 100
        self.age = self.age + 0.25
        self.qualification = self.qualification + random.uniform(-0.2, 0.2)
        if self.age <= 18:
            self.height = self.height + random.uniform(0.003, 0.008)  # girl
            self.weight = self.weight + random.uniform(0.8, 1.5)
        else:
            self.weight = self.weight + random.uniform(0.2, 0.4)

    def hm_work(self):
        if self.show_info:
            print("正在工作")
            print("时间过去了3个月")
            print("你的属性发生了变化")
        self.qualification = self.qualification + random.uniform(-0.2, 0)
        self.money = self.money + self.qualification * 100
        self.weight = self.weight + random.uniform(-0.5, 0.5)

    def __init__(self, name, age, sex, height, weight, qualification):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.qualification = qualification
        self.money = 5000
        self.show_info = True
        self.alive = True

    def human_bmi(self, check_status=False):
        bmi = self.weight / (self.height * self.height)
        if check_status:
            return bmi
        print("你的身高：%.2f,你的体重%.2f,BMI指数%.2f" % (self.height, self.weight, bmi))

        if bmi >= 35:
            print("超胖")
        elif 30 <= bmi < 35:
            print("肥胖")
        elif 25 <= bmi < 30:
            print("过重")
        elif 18.5 <= bmi < 25:
            print("适中")
        elif 10 <= bmi < 18.5:
            print("过轻")
        else:
            print("健康异常,你GG")

    def hm_show(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.sex)
        print("身高：", self.height)
        print("体重：", self.weight)
        print("资质：", self.qualification)
        print("资产：", self.money)
        self.human_bmi()

    def hm_die(self):
        self.alive = False

if __name__ == "__main__":
    dagou = humanBase("大狗", 20, "boy", 1.77, 70)
    dagou.human_bmi()
