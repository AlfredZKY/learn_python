# a = 100
# sum = 0
# i = 0
# while True:
#     if i == 2000:
#         break
#     sum += a
#     a += 100
#     i += 1
#     print('第{0}天产出的 psersent is {1}'.format(i, sum/100000000))


<<<<<<< HEAD
# def fib():
#     a, b = 0, 1
#     while 1:
#         if b > 100000000000:
#             break
#         yield b
#         a, b = b, a+b

# for i in fib():
#     print(i," ")

import lxml.html

etree = lxml.html.etree

with open('F:/my_project/learn_python/000737+2018年年度报告+2019-03-05+1205874756.html','r',encoding='utf8') as f:
    page = f.read()
    html = etree.HTML(page)
    ps = html.xpath('//P')
    for item in ps:
        print(item.string())
=======
def fib():
    a, b = 0, 1
    while 1:
        if b > 100000000000:
            break
        yield b
        a, b = b, a+b

for i in fib():
    print(i," ")
print("hello world")

>>>>>>> 12203ac55bede5d5e05ae0e0db5b392180e20b2f
