from tqdm import tqdm

from time import sleep
from progressbar import *

def tqdm_bar():
    for i in tqdm(range(int(9e6))):
        pass


# widgets可选参数含义：
# 'Progress: ' ：设置进度条前显示的文字
# Percentage() ：显示百分比
# Bar('#') ： 设置进度条形状
# ETA() ： 显示预计剩余时间
# Timer() ：显示已用时间 

total = 1000
widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*total).start()  

def progress_bar():
    total = 1000
    for i in range(total):
        pbar.update(10*i + 1)
        time.sleep(0.01)


def my_process_bar(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('[', '#' * left, ' ' * right, ']',f'{percent:.0f}%', sep='', end='', flush=True)

if __name__ == '__main__':
    progress_bar()
    pbar.finish()
    # for i in range(101):
    #     my_process_bar(i)
    # sleep(0.1)