import chardet
import jieba
import os

# chardet 模块应用背景，如果要对一个大文件进行编码识别，
# 使用这种高级的方法，可以只读一部，去判别编码方式从而提高检测速度。
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path

# 获取当前文件的路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
print(d)
# 获取文本txt
# text = open(path.join(d, r'file/langchao.txt'),encoding='utf-8').read()
text = open(path.join(d, r'file/langchao.txt'),'rb').read()

# print(text)

text_charInfo = chardet.detect(text)
print(text_charInfo)
# text += ''.join(jieba.cut())

text = open(path.join(d, r'file/langchao.txt'),encoding='UTF-8-SIG').read()
text = open(path.join(d, r'file/langchao.txt'),encoding='utf-8').read()
# print(text)
