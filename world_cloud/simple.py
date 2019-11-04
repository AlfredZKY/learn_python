import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt

# 获取当前文件的路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
print(d)
# 获取文本txt
text = open(path.join(d, r'file/legend1900.txt')).read()

# 生成词云，背景色为灰色
wc = WordCloud(scale=2,# 缩放2倍
               max_font_size=100,
               background_color='#383838', # 灰色
               colormap='Blues')
wc.generate_from_text(text)

# 显示图像
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()

# 存储图像
wc.to_file(d + r'\1900_basic.png')
# or plt.savefig('1900_basic.png,dpi=200)

plt.show()
