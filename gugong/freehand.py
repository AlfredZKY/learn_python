from PIL import Image
import numpy as np
import os
import join
import time

# 转化为二维灰度图片
# im = Image.open('./gugong/data/photo.jpg').convert("L")
# a = np.asarray(im).astype('float')
# print(a.shape,a.dtype)

# 实现图像手绘
# 梯度的重构
# numpy的梯度函数的介绍
# np.gradient(a) ： 计算数组a中元素的梯度，f为多维时，返回每个维度的梯度
# 离散梯度： xy坐标轴连续三个x轴坐标对应的y轴值：a, b, c 其中b的梯度是（c-a）/2
# 而c的梯度是： (c-b)/1
# 当为二维数组时，np.gradient(a) 得出两个数组，第一个数组对应最外层维度的梯度，第二个数组对应第二层维度的梯度。


def image(sta, end, depths):
    a = np.asarray(Image.open(sta).convert('L')).astype('float')
    depth = depths # 深度的取值范围(0-100),标准取10
    grad = np.gradient(a) # 取图像灰度的梯度值
    grad_x,grad_y=grad # 分别取纵横图像梯度值
    grad_x = grad_x * depth / 100 # 对grad_x值进行归一化
    grad_y = grad_y * depth / 100 # 对grad_x值进行归一化
    A = np.sqrt(grad_x **2 + grad_y **2 + 1.)
    uni_x = grad_x /A
    uni_y = grad_y /A
    uni_z = 1. / A
    vec_el = np.pi / 2.2    # 光源的俯视角度，弧度制
    vec_az = np.pi / 4.     # 光源的方位角度，弧度制
    dx = np.cos(vec_el) * np.cos(vec_az) # 光源对x轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az) # 光源对y轴的影响
    dz = np.sin(vec_el) # 光源对z轴的影响
    b = 255 * (dx * uni_x + dy*uni_y + dz * uni_z) # 光源归一化
    b = b.clip(0,255)
    im = Image.fromarray(b.astype('uint8')) # 重构图像
    im.save(end)

def main():
    xs = 10
    start_time = time.clock()
    startss = os.listdir(
        r'E:\BaiduNetdiskDownload\project\learn_python\gugong\data')
    time.sleep(2)
    for starts in startss:
        start = ''.join(starts)
        sta = 'E:/BaiduNetdiskDownload/project/learn_python/gugong/data/' + start
        end = 'E:/BaiduNetdiskDownload/project/learn_python/gugong/data/' + 'HD_' + start
        image(sta=sta, end=end, depths=xs)

    end_time = time.clock()

    print('程序运行了 ----' + str(end_time-start_time) + '秒')
    time.sleep(3)


if __name__ == '__main__':
    main()
