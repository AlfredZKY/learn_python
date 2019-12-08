from bs4 import BeautifulSoup
import bs4
import re
html = """
<html>
<head><title>The Dormouse's story</title>
</head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span> Elsie </span></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

html1 = """
<html>
<head><title>The Dormouse's story</title>
</head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span> Elsie </span></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

html2 = """
<html>
<head><title>The Dormouse's story</title>
</head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span> Elsie </span>
</a>
</p>
<p class="story">...</p>
"""

html3 = """
<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span> Elsie </span>
</a>
hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
"""

html4 = """
<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
"""

soup = BeautifulSoup(html,'lxml')
soup1 = BeautifulSoup(html1,'lxml')
soup2 = BeautifulSoup(html2,'lxml')
soup3 = BeautifulSoup(html3,'lxml')
soup4 = BeautifulSoup(html4,'lxml')

def select_element():
    # soup = BeautifulSoup('<p>hello</p>','lxml')
    print(soup.p.string)

    # 把解析的字符串以标准的缩进格式输出,包括对不标准的HTML格式的自动更正格式。
    print(soup.prettify())

    # 提取到title的文本
    print(soup.title.string)
    print(type(soup.title))

    # 打印出节点内容
    print(soup.title)
    print(soup.head)

    # 当存在多个节点时，默认输出第一个节点 
    print(soup.p)

def select_info():
    # 获取名称
    print(soup.title.name)

    # 获取属性,如果一个节点存在多个属性时，比如id和class等，选择这个节点元素后，可以调用attrs获取所有属性
    print(soup.p.attrs)
    print(soup.p.attrs['name'])
    print(soup.p['name'],'\t',soup.p['class'])

    # 获取内容: 利用string属性获取节点元素包含的文本内容，比如要获取第一个p节点的文档
    print(soup.p.string)

def select_node_info():
    # 获取子节点和子孙节点,返回第一个p节点的直接子节点包含的所有的信息
    print(soup1.p.contents)

    # 返回直接子节点的列表
    print(soup1.p.children)
    for i,child in enumerate(soup1.p.children):
        print(i,child)

    # 返回所有的子孙节点,descendants递归遍历所有子节点
    print(soup1.p.descendants)
    for i,child in enumerate(soup1.p.descendants):
        print(i,child)

def get_parent_node():
    print('*****************************')
    # 获取某个节点元素的父节点，可以调用parent属性
    print(soup2.a.parent)
    print(list(enumerate(soup2.a.parents)))

def get_friend_node():
    print('------------------------')
    print('Next Sibling','\t',soup3.a.next_sibling)
    print('Prev Sibling','\t',soup3.a.previous_sibling)

    print('Next Siblings','\t',list(enumerate(soup3.a.next_siblings)))
    print('Prev Siblings','\t',list(enumerate(soup.a.previous_siblings)))

def get_node_info():
    print('==========================')
    print('Next Sibling')
    print(type(soup4.a.next_sibling))
    print(soup4.a.next_sibling.string)
    print('Parnt::')
    print(type(soup4.a.parents))
    print(list(soup4.a.parents)[0])
    print(list(soup4.a.parents)[0].attrs['class'])


html5='''
<div class ="panel">
<div class ="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo link</li>
<li class="element">Bar is link</li>
</ul>
</div>
</div>
'''
soup5 =BeautifulSoup(html5,'lxml')

# 方法选择器
def select_func():
    # find_all 查找所有符合条件的元素，给它传入一些属性或文本，就可以得到符合条件的元素
    # find_all(name,attrs,recursive,text,**kwargs)
    print('----------------------------------')
    # 通过节点名字搜寻
    for ul in soup5.find_all(name='ul'):
        print(ul.find_all(name='li'))
        for li in ul.find_all(name='li'):
            print(li.string)

    print(type(soup5.find_all(name='ul')[0]))

    # 通过属性值来查询
    print(soup5.find_all(attrs={'id':'list-1'}))
    print(soup5.find_all(attrs={'name':'elements'}))
    print(soup5.find_all(class_='element'))
    print(type(soup5.find_all(attrs={'id':'list-1'})[0]))
    
    # 通过text查询
    print(soup5.find_all(text=re.compile('link')))

if __name__ == '__main__':
    select_element()
    select_info()
    select_node_info()
    get_parent_node()
    get_friend_node()
    get_node_info()
    select_func()