import copy
import keyword

data = ["1", "2", "3", "4", "5", "6", "7"]


def listCreate(data):
    new_data = list(input("请输入列表用;隔开：").split(";"))
    new_data_len = len(new_data)
    # print(new_data,new_data_len)
    if new_data_len > 1:
        data.clear()
        while new_data_len > 0:
            data.append(new_data.pop(0))
            new_data_len = new_data_len - 1
    else:
        print("未操作")
    # data.append(new_data.)
    # data = copy.deepcopy(new_data)


def listRead(data):
    id = int(input("请输入要读取的id:")) - 1
    try:
        print(data[id])
    except IndexError:
        print("没有这个id,请重新尝试")


def listUpdate(data):
    up_value = str(input("请输入要替换的值用;隔开:")).split(";")
    # print(upValue)
    try:
        id = data.index(up_value[0])
        data[id] = up_value[1]
    except ValueError:
        print("没有找到这个值，请重新尝试！")

    # except:


def listDelete(data):
    del_value = str(input("请输入要删除的元素:"))
    try:
        data.remove(del_value)
    except ValueError:
        print("没有找到这个值，请重新尝试！")


def listCUDI(data):
    """
    列表的增删改查（CRUD）简单实现，传入一个列表
    :param data:
    :return:
    """
    while True:
        # 将所有输入转成小写，处理大小写问题
        cmd = str(input("请输入要执行的操作CRUD,或者Q退出：")).lower()
        if cmd == "c":
            listCreate(data)
        elif cmd == "r":
            listRead(data)
        elif cmd == "u":
            listUpdate(data)
        elif cmd == "d":
            listDelete(data)
        elif cmd == "q":
            print("退出程序")
            break
        else:
            pass
        print(data)

    # 列表倒置
    # data.reverse()
    # 升降序排序，元素是同类型，否则会报错
    # data.sort()


if __name__ == "__main__":
    # print(type(data))
    listCUDI(data)
