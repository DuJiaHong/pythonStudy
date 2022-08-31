# 打印三角函数
# 倒立等边三角形
def start_print():
    star = int(input("请输入三角形阶数："))
    half_star = star
    while star > 0:
        for i in range(half_star - star):
            print(" ", end="")

        for i in range(star):
            print("* ", end="")
        print("")
        star = star - 1


if __name__ == "__main__":
    start_print()
