# 随机函数实现猜拳
import random


def mora():
    print("这个是个简易的石头剪刀布游戏")
    print("1：石头，2：剪刀，3：布")
    a = {1: "石头", 2: "剪刀", 3: "布"}
    while True:
        guss = random.randint(1, 3)
        # print(guss)
        client = int(input("请输入："))
        print("电脑出：%s，你出了：%s" % (a.get(guss), a.get(client)))
        if guss == client:
            print("和电脑出的一样，真是心有灵犀啊！")
            continue
        elif (guss - client) == 1 or (client - guss) == 2:
            print("你赢了")
            break
        else:
            print("猜错了，请继续")


if __name__ == "__main__":
    mora()
