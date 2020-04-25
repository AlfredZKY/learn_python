from pyquery import PyQuery as pq 

html1 = '''
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
'''



html2 = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 解析网页网页全部采用css 选择器

def learn_pq():
    doc = pq(html1)
    print(doc('a'))
    doc = pq(html2)
    print(doc('li'))
    
    # pyquery 可以传入一个url 
    doc = pq(url = "https://cuiqingcai.com")
    print(doc("title").text())

    # 传入文件
    doc = pq(filename='parsehtml/learn_pquery/html1.html')
    print(doc('li'))

select_html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

def use_css_selector():
    doc = pq(select_html)
    # 通过选择器 id #idname
    # 先选取id为container的节点，然后再选取其内部class为list的所有li节点
    print([item.text() for item in doc('#container .list li').items()])

def search_child_node():
    # 子节点
    doc = pq(select_html)
    items = doc('.list')
    print(type(items))
    print(items)
    # find是查找范围是所有的所有子孙节点 如果只是想查找子节点可以使用children
    lis = items.find('li')
    print(lis)
    print(type(lis))

    # 传入要查找的条件即可
    lis_child = items.children('.active')
    print(type(lis_child))
    print(lis_child)

parent_html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

def search_father_node():
    # 查找节点对应父节点
    # 先查找class为list的节点，然后调用parent方法得到其直接父节点，其类型依然是pyquery类型，调用parents可以得到祖宗节点
    doc = pq(parent_html)
    items = doc('.list')
    container = items.parent()
    print(container)
    print(type(container))

    # 可以传入搜索条件
    # parents = items.parents('.wrap')
    parents = items.parents('.container')
    print(parents)
    print(type(parents))


def search_brother_node():
    doc = pq(parent_html)
    li = doc('.list .item-0.active')
    print(li.siblings('.active'))

def traverse_node():
    doc = pq(parent_html)
    lis = doc('li').items()
    print(type(lis))
    for li in lis:
        print(li('.item-0'),type(li))

def get_attr_info():
    doc = pq(parent_html)
    a = doc('.item-0.active a')
    print(a,type(a))
    print(a.attr('href'))

if __name__ == '__main__':
    # learn_pq()
    # use_css_selector()
    # search_child_node()
    # search_father_node()
    # search_brother_node()
    # traverse_node()
    get_attr_info()