import os

# 以txt文本保存在本地
path = os.getcwd() + "\studentInfo.txt"


def load_data():
    f = open(path, "r", encoding='UTF-8')
    info = []
    for line in f.readlines():
        r_info = line.strip().split(";")
        stu_key = {}
        for i in range(len(r_info) - 1):
            key_info = r_info[i].split(",")
            # print("value ",key_info)
            # print("info ",len(r_info))
            # print("read key ",key,"  value  ",value)
            stu_key[key_info[0]] = key_info[1]
            # print(stu_key)
        info.append(stu_key)
    f.close()
    return info


def save_data(info):
    f = open(path, "w", encoding='UTF-8')
    print("save info size ", len(info))
    for i in range(len(info)):
        for key, value in info[i].items():
            # print(key+","+value+"\r")
            f.write(key + "," + value + ";")
        f.write("\r")
    f.close()


def update_student(info):
    name = str(input("请输入要更新学生姓名："))
    for i in range(len(info)):
        if name in info[i].get("name"):
            print("已找到用户该学生信息。")
            name = str(input("请输入要更新学生姓名："))
            age = str(input("请输入要更新学生年龄："))
            stu_info = {"name": name, "age": age}
            print(stu_info)
            value = str(input("是否更新当前数据(Y?N)")).lower()
            if value == 'y':
                info[i] = stu_info
            break
    print("未找到该用户信息。")


def del_student(info):
    name = str(input("请输入要删除学生姓名："))
    # print(name)
    for i in range(len(info)):
        # print("remove this list ",info[i])

        if name in info[i].get("name"):
            info.pop(i)
            print("删除成功")
            break


def add_student(info):
    name = str(input("请输入姓名："))
    age = str(input("请输入年龄"))
    stu_info = {"name": name, "age": age}

    print(stu_info)
    value = str(input("是否添加当前数据(Y?N)")).lower()
    if value == 'y':
        info.append(stu_info)


def studentInfo():
    """
    学生信息系统，信息保存在当前目录studentInfo.txt
    内容格式为：
        name,xxxx;age,88;
        name,ddd;age,22;
        name,55;age,44;
    :return:
    """
    # 判断本地数据文件是否存在，否则则创建一个空的列表
    if os.path.exists(path):
        info = load_data()
    else:
        info = ()
    print("欢迎登陆学生信息系统")
    while True:
        print("1.学生信息查看")
        print("2.学生信息删除")
        print("3.学生信息添加")
        print("4.学生信息更新")
        print("5.退出系统")
        value = str(input("请输入选择项（1-5）:"))
        if value == '1':
            print(info)
        elif value == '2':
            del_student(info)
        elif value == '3':
            add_student(info)
        elif value == '4':
            update_student(info)
        elif value == '5':
            value = str(input("是否保存当前数据(Y?N)")).lower()
            if value == 'y':
                save_data(info)
                break
            elif value == 'n':
                break
            else:
                continue
        else:
            continue


if __name__ == "__main__":
    studentInfo()
