# beautiful soup解析器  
|解析器|使用方法|优势|劣势|  
|:-----|:-----|:-----|:-----|  
|Python标准库|BeautifulSoup(markup,"html.parse")|Python内置标准库，执行速度适中，文档容错能力强|Python2.7.3及Python3.2.2之前的版本文档容错能力差|
|lxmlHTML解析器|BeautifulSoup(markup,"lxml")|速度快、文档容错能力强|需要C语言库|
|xmlHTML解析器|BeautifulSoup(markup,"xml")|速度快、唯一支持XML的解析器|需要C语言库|
|html5lib|BeautifulSoup(markup,"html5lib")|最好的容错性，以浏览器的方式解析文档、生成HTML5格式的文档|速度慢、不依赖外部扩展|

# 节点选择器
直接调用节点的名称就可以选择节点元素，再调用string属性就可以得到节点内的文本，这种选择方式速度非常快，如果单个节点结构层次非常清晰，可以选用这种方式来解析。  
