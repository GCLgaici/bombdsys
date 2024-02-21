import random
from pynput.keyboard import Key, Controller
from function.show import fy, try_convert_to_int, fr, bs_help



class Sys:
    def __init__(self):
        # 模拟键盘的按键和释放操作
        self.keyboard = Controller()

        # 不好听数据库
        self.not_good_database = [
            "不是吧，你干嘛呢？",
            "666",
            "sb吧",
            "CMD",
            "Bad brain",
        ]
        # 自定义数据库
        self.custom_databases = []

    def random(self, num_cz, data):
        fy()
        # 随机轰炸
        if len(num_cz) != 4:
            frequency = 20
        else:
            frequency = try_convert_to_int(num_cz[3])

        for _ in range(frequency):
            self.keyboard.type(data[random.randint(0, len(data) - 1)])
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)

    def Introduction(self, data):
        fy()
        # 顺序轰炸
        for m_str in data:
            self.keyboard.type(m_str)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)


def main():
    sys = Sys()
    while True:
        cz = input("[BS]:>>").split(" ")
        if cz[0] == "help":
            if bs_help(cz):
                print("""
有关某个命令的详细信息，请键入 help 命令名(
For more information about a command, type the: help cmd-na
    run         运行轰炸脚本
    exit        退出/关闭窗口

                """)

        elif cz[0] == "exit":
            break
        elif cz[0] == "r" or cz[0] == "run" or cz[0] == "Run":
            # 找库
            temp_databases = []
            if cz[1] == "god":
                temp_databases = fr('database/good.bd').split('\n')
            elif cz[1] == "ngd":
                temp_databases = sys.not_good_database
            elif cz[1] == "ctd":
                temp_databases = sys.custom_databases
            else:
                temp_databases = fr(cz[1]).split('\n')

            # 提取方式
            if cz[2] == "r":
                sys.random(cz, temp_databases)
            elif cz[2] == "i":
                sys.Introduction(temp_databases)


if __name__ == '__main__':
    main()
