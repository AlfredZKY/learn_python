'''
@Description: 
@Author: zky
@Date: 2019-11-09 09:53:34
@LastEditTime: 2019-11-09 14:18:56
@LastEditors: huacong
'''

# 此方法与平台无关（ANSI序列不会在支持它们的终端上修改），并允许您在字符串中使用原始ANSI序列，以及为您提供颜色定义。
import colorama
colorama.init()

'''
@description: 
@param : 
@return: 
'''
def esc(code=0):
    '''
    :param code:
    :return:
    '''
    return '\033[{0}m'.format(code)

# 说明：
# 前景色            背景色           颜色
# ---------------------------------------
# 30                40              黑色
# 31                41              红色
# 32                42              绿色
# 33                43              黃色
# 34                44              蓝色
# 35                45              紫红色
# 36                46              青蓝色
# 37                47              白色

# 显示方式           意义
# -------------------------
# 0                终端默认设置
# 1                高亮显示
# 4                使用下划线
# 5                闪烁
# 7                反白显示
# 8                不可见

# 例子：
# [1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->


def print_color_font():
    print(esc('1;31;40')+'Error:'+esc()+'import')
    print("\033[1;32;40m================signing====================\033[m")
    print('This is a \033[1;35m test \033[0m!')
    print('\033[1;31;40m')
    print('*' * 50)
    print('*HOST:\t', 2002)
    print('*URI:\t', 'http://127.0.0.1')
    print('*ARGS:\t', 111)
    print('*TIME:\t', '22:28')
    print('*' * 50)
    print('\033[0m')


# from blessings import Terminal

# term = Terminal()
# print(term.red("hello"), term.green("world"))

if __name__ == '__main__':
    # print_color_font()
    pass