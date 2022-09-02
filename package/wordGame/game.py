import random

# from humanBase import humanBase
import package

def hum_init():
    print("初始化人物状态")
    hm_name = str(input("请输入主人公姓名："))
    hm_sex = str(input("请输入主人公性别："))

    hm_data = package.humanBase(hm_name, 8, hm_sex, random.uniform(1.21, 1.32), random.randint(21, 30), random.randint(0, 9))
    hm_data.human_bmi()
    hm_data.hm_show()
    return hm_data


def gm_one_year(hm_data):
    """
    随机产生1年的经历用于快速迭代测试
    :param hm_data:
    :return:
    """
    for i in range(4):
        # print("%d岁，第%d季度" % (hm_data.age, i))
        hm_data.show_info = False
        if hm_data.age >= 16:
            can_do = 4
        else:
            can_do = 3
        choose = random.randint(1, can_do)
        if choose == 1:
            hm_data.hm_sport()
        elif choose == 2:
            hm_data.hm_study()
        elif choose == 3:
            hm_data.hm_sleep()
        elif choose == 4:
            hm_data.hm_work()

        if gm_over(hm_data):
            break


def gm_ten_year(hm_data):
    for i in range(10):
        print("日复一年又一年 %d" % i)
        gm_one_year(hm_data)


def gm_over(hm_data):
    if hm_data.age > 40:
        print("年纪到了，该退休了！")
        hm_data.hm_die()
        return True
    elif hm_data.money <= 0:
        print("穷苦潦倒，GG.....")
        hm_data.hm_die()
        return True
    elif hm_data.human_bmi(True) < 10:
        print("太瘦了,你饿死了...")
        hm_data.hm_die()
        return True
    else:
        return False


def gm_start():
    hm_data = hum_init()
    run_game = hm_data.alive
    while run_game:
        print("开始选择培养方向")
        print("1. 运动")
        print("2. 学习")
        print("3. 休息")
        print("4. 显示当前状态信息")
        print("5. 10年一梦")
        choose = str(input("请输入:"))
        if choose == '1':
            hm_data.hm_sport()
        elif choose == '2':
            hm_data.hm_study()
        elif choose == '3':
            hm_data.hm_sleep()
        elif choose == '4':
            hm_data.hm_show()
        elif choose == '5':
            gm_ten_year(hm_data)
        print("hm status ", hm_data.alive)
        if hm_data.age >= 45 or bool(1 - hm_data.alive):
            print("Game Over")
            hm_data.hm_show()
            break


def gm_init():
    while True:
        print("1. 开始游戏")
        print("2. 加载存档")
        print("2. 退出游戏")
        choose = str(input("请输入:"))
        if choose == '1':
            gm_start()
        if choose == '2':
            print("正在开发中。。。。")
            continue
        elif choose == '3':
            print("已退出！")
            break
        else:
            continue


def game():
    gm_init()


if __name__ == "__main__":
    gm_init()
