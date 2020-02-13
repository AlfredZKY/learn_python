from lxml import etree

html1 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

text  = '''
<div>
<Ul>
<li class="item-0"><a href="link1.html ">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

text1  = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

text2  = '''
<li class="li li-first" name="item"><a href="link.html">second item</a></li>
'''

html = etree.HTML(text,etree.HTMLParser())

# 会对不完整的html文档进行恢复
def print_info():
    # html = etree.HTML(text)
    html = etree.HTML(text,etree.HTMLParser())
    result = etree.tostring(html)
    print(result.decode('utf-8'))

# 选取所有的节点信息
def select_all_node():
    res = html.xpath('//*')
    print(res)

# 选取所有的li节点信息
def sel_li_node():
    # 这里要选取所有的li节点，可以使用//，然后直接加上节点名称即可，调用时直接使用xpath()方法即可
    res = html.xpath('//li')
    print(res)
    print(res[0])

def sel_ul_child_node():
    # 这里要选取所有的ul节点下的a节点，可以使用//，然后直接加上节点名称即可，调用时直接使用xpath()方法即可
    # 因为a不是ul的直接子节点，所有结果为null
    # res = html.xpath('//ul/a')
    res = html.xpath('//ul//a')
    print(res)

def get_attr_parent_node():
    # 通过已知属性href="link4.html"的一个节点，然后查找它的父节点
    res = html.xpath('//a[@href="link4.html"]/../@class')
    print(res)
    # 通过parent::来获取父节点
    res = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    print(res)

def get_attr_node():
    # 选取class是item-1的li节点
    res = html.xpath('//li[@class="item-1"]')
    print(res)

def get_text_from_node():
    # 获取li节点中的文本,以下两种方式，
    # 第一种定点取出对应节点文本整洁
    # 第二种取出所有的节点文本内容，如果文档不整洁，容易取出一些换行符等特殊字符
    res = html.xpath('//li[@class="item-0"]/a/text()')
    print(res)

    res = html.xpath('//li[@class="item-0"]//text()')
    print(res)

def get_attr():
    # 获取li节点下所有a节点的href属性
    res = html.xpath('//li/a/@href')
    print(res)

def get_attr_multi():
    # 属性多值匹配
    # 获取到li节点class属性有两个值li和li-first 需要contains函数
    html = etree.HTML(text1,etree.HTMLParser())
    res = html.xpath('//li[contains(@class,"li")]/a/text()')
    print(res)

    # 多属性匹配
    html = etree.HTML(text2,etree.HTMLParser())
    res = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
    print(res)

if __name__ == '__main__':
    print_info()
    select_all_node()
    sel_li_node()
    sel_ul_child_node()
    get_attr_parent_node()
    get_attr_node()
    get_text_from_node()
    get_attr()
    get_attr_multi()