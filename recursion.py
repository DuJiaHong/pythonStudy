# def han_nuo_ta():
#
#

def test2(a):
    # 斐波那契数列
    # 1,1,2,3,5,8,13,21...
    if a == 1 or a == 2:
        return 1
    return test2(a - 1) + test2(a -2)


def test1(a):
    # a阶乘
    if a == 1:
        return 1
    return a * test1(a - 1)


def recursion():
    """
    递归函数测试
    test1 阶乘
    test2 斐波那契数列
    :return:
    """
    vale = test2(3)
    print(vale)
    ff = []
    for i in range(1,10):
        ff.append(test2(i))
    print(ff)


if __name__ == "__main__":
    recursion()
