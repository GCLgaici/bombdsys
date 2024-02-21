import time


def fy():
    print("""
    --------------------------
    数据已接收！请将光标移动到会话框
       并将输入法切换至英文状态
    --------------------------
    """)
    time.sleep(2)
    for i in range(3):
        print(r'距离程序运行还有%d秒！' % (3 - i))
        time.sleep(1)

def try_convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return 20
def fr(path):
    f = open(path, 'r', encoding='utf-8')
    # 读取文件内容
    text = f.read()
    f.close()
    return text

def bs_help(num_cz):
    if len(num_cz) == 1:
        return True
    print("""
                根据数据与参数运行脚本

                run database Output_mode [frequency]

                Chinese
                    示例：   run god r 30
                            run ctd i
                    # run +数据库(可以是数据库文件路径) +输出方式(r是随机输出i是遍历输出)

                English
                    example：    run god r 30
                                 run ctd i
                    # run +Database (can be a database file path) +Output mode (r is random output, i is traversal output)
                """)
    return None

