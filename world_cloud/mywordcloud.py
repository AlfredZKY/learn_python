'''
    wordcloud 词云绘制
    1.英文词云 text
    2.中文词云 text
    3.根据词频绘图
'''

import chardet
import os
import random
import chardet
import jieba
import numpy as np 
import pandas as pd 

from os import path
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt 
from scipy.misc import imread



# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text
text = open(path.join(d + '/file/legend1900.txt')).read()

def wc_english_basic():
    # 生成词云
    wc = WordCloud(
        scale=2,
        max_font_size=100,
        background_color='white',
        colormap='Blues'
    )
    wc.generate_from_text(text)

    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

    # 存储图像
    wc.to_file('1900_basic2.png')
    # or
    # plt.save_file('1900_basic2.png',dpi=200)
    plt.show()

def wc_english_improve1():
    # 读取背景图片
    background_Image = np.array(Image.open(path.join(d,"mask1900.jpg")))
    # or
    # background_Image = imread(path.join(d, "mask1900.jpg"))
    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)

    # 设置英文停止词
    stopwords = set(STOPWORDS)
    stopwords.add('one')
    wc = WordCloud(
        # font_path = font_path,
        margin=2, # 设置页面边缘
        mask=background_Image,
        scale=2,
        max_words=200, # 设置最多词个数
        min_font_size=4, # 设置最小字体大小
        max_font_size=150, # 设置最大字体大小
        stopwords=stopwords, # 设置停止词
        random_state= 42, #设置随机值
        background_color='white' # 设置背景色
    )

    # 生成词云 等价于 wc.generate(text)
    wc.generate_from_text(text)

    # 获取文本词排序，用于调整 stopwords
    process_words = WordCloud.process_text(wc,text)
    sort = sorted(process_words.items(),key=lambda x:x[1],reverse=True)
    # print(sort[:50])

    # 根据图片色设置背景色
    wc.recolor(color_func=img_colors)

    # 存储图像
    wc.to_file('1900pro.png')

    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def wc_english_improve2():
    # 读取背景图片
    background_Image = np.array(Image.open(path.join(d,"mask1900.jpg")))
    # or
    # background_Image = imread(path.join(d, "mask1900.jpg"))
    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)

    # 设置英文停止词
    stopwords = set(STOPWORDS)
    stopwords.add('one')
    wc = WordCloud(
        # font_path = font_path,
        margin=2, # 设置页面边缘
        mask=background_Image,
        scale=2,
        max_words=200, # 设置最多词个数
        min_font_size=4, # 设置最小字体大小
        max_font_size=150, # 设置最大字体大小
        stopwords=stopwords, # 设置停止词
        random_state= 42, #设置随机值
        background_color='white' # 设置背景色
    )

    # 生成词云 等价于 wc.generate(text)
    wc.generate_from_text(text)

    # 获取文本词排序，用于调整 stopwords
    # process_words = WordCloud.process_text(wc,text)
    # sort = sorted(process_words.items(),key=lambda x:x[1],reverse=True)
    # print(sort[:50])

    # 根据图片色设置背景色
    def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(50,100)

    wc.recolor(color_func=grey_color_func)

    # 存储图像
    wc.to_file('1900pro2.png')

    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def wc_chinse():
    # 获取文本text,确定编码格式
    # text = open(path.join(d,'/file/langchao.txt')),'rb').read()
    # text_charInfo = chardet.detect(text)
    # print(text_charInfo)

    text = open(path.join(d+'/file/langchao.txt'),encoding='UTF-8-SIG').read()
    # 进行分词
    text = ' '.join(jieba.cut(text,cut_all=False))
    # print(text)
    # 设置中文字体
    font_path = r'C:\Windows\Fonts\STFANGSO.TTF'

    # 读取背景图片
    background_Image = np.array(Image.open(path.join(d,"mask1900.jpg")))
    # or
    # background_Image = imread(path.join(d, "mask1900.jpg"))
    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)

    # 设置自定义词典
    jieba.load_userdict(path.join(d+'/file/userdict.txt'))
    jieba.add_word('因特尔')

    # 设置中文停止词
    stopwords = set('')
    stopwords.update(['但是','一个','自己','因此','没有','很多','可以','这个','虽然','因为','这样','已经','现在','一些','比如','不是','当然','可能','如果','就是','同时','比如','这些','必须','由于','而且','并且','他们'])

    wc = WordCloud(
        font_path=font_path, # 设置中文路径
        margin=2,
        mask=background_Image,
        scale=2,
        max_words=200,
        min_font_size=4,
        max_font_size=100,
        stopwords=stopwords,
        random_state=42,
        background_color='white',
    )
    
    # 生成词云
    wc.generate_from_text(text)

    # 设置词云背景色，如不想要背景图片颜色，就注释掉
    wc.recolor(color_func=img_colors)

    # 存储图像

    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def wc_dataframe():
    df = pd.read_csv(path.join(d+'/file/university.csv'),encoding='utf-8')
    df = df.groupby(by='country').count()
    df = df['world rank'].sort_values(ascending=False)
    font_path = r'C:\Windows\Fonts\STFANGSO.TTF'
    # print(df)
    wc = WordCloud(
        font_path=font_path,
        background_color = '#F3F3F3',
        width=500,
        height=300,
        margin=2,
        max_font_size=200,
        random_state=42,
        scale=2,
        colormap='viridis',
    )

    wc.generate_from_frequencies(df)

    wc.to_file('university.png')

    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    # print(d)
    # print(text)
    # wc_english_basic()
    # wc_english_improve1()
    # wc_english_improve2()
    # wc_chinse()
    wc_dataframe()

if __name__ == '__main__':
    main()