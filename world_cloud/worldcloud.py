import os
import numpy as np
import random

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
# from scipy.misc import imread


def wc_english():
    # 获取当前文件的路径
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # 获取文本txt
    text = open(path.join(d, r'world_cloud\file\legend1900.txt')).read()

    # 读取背景图片
    background_Image = np.array(Image.open(
        path.join(d, r'world_cloud\mask1900.jpg')))

    # 提取背景图片颜色
    img_color = ImageColorGenerator(background_Image)

    # 设置英文停止词,用词云自带的停止词
    stopwords = set(STOPWORDS)
    stopwords.add('one')
    wc = WordCloud(
        margin=2,  # 设置页面边缘
        mask=background_Image,  # 设置背景图片
        scale=2,  # 设置缩放倍数
        max_words=200,  # 设置最多次个数
        min_font_size=4,  # 设置最小字体大小
        max_font_size=150,  # 设置最大字体大小
        stopwords=stopwords,
        random_state=42,
        background_color='white',  # 背景颜色
        colormap='Blues')

    # 删除词频出现的one
    # 获取文本词排序，来调整stopword
    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)

    # 生成词云
    wc.generate_from_text(text)

    # 根据图片色设置背景色,根据图片色彩绘制词云文字颜色
    # wc.recolor(color_func=img_color)
    wc.recolor(color_func=grey_color_func)
    # 显示图像 interpolation 内插入法 bilinear双线性
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

    # 存储图像
    wc.to_file(d + r'\world_cloud\1900pro1.png')
    # or plt.savefig('1900_basic.png,dpi=200)

    plt.show()


def grey_color_func(word, font_size, position, orientation, rando_state=None, **kwargs):
    return "hsl(0,0%%,%d%%)" % random.randint(50, 100)


if __name__ == "__main__":
    wc_english()
