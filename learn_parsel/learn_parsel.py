from parsel import Selector

import requests

url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'

'''<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>'''

sel = Selector(requests.get(url).text)
print(sel.xpath('//title/text()').getall())
print(sel.xpath('//title/text()').get())

print(sel.css('title::text').get())

print([img.attrib['src'] for img in sel.css('img')])
print(sel.css('img')[2].attrib['src'])
# *::text 选择当前选择器上下文的所有后代文本节点：'
print(sel.css('title::text').get())
print(sel.css('a::attr(href)').getall())