import os

lis = [23,45,1,2,56,87,-2,0,100]
# 冒泡排序
def sortport(lis):
    for i in range(len(lis) - 1):
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis

# 计算x的n次方
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

# 计算a*a + b*b + c*c + ……
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 计算阶乘 n!
def fac():
    num = int(input("请输入一个数字: "))
    factorial = 1
    # 查看数字是负数，0或正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1,num+1):
            factorial = factorial * i
        print("%d的阶乘 %d " % (num,factorial))

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

# 列出当前目录下的所有文件和目录名
def show_dir(filepath=r"F:\\my_project\\learn_python\\"):
    # print([d for d in os.listdir('.') ])
    # path = input("请输入一个路径:")
    if filepath == "":
        print("请输入正确的路径")
    else:
        for i in os.listdir(filepath): # 获取目录中的文件及其子目录
            path = (os.path.join(filepath,i))
            if os.path.isdir(path):
                show_dir(path)
            if path.endswith(".html"):
                print(path)

# 把一个list中所有的字符串变成小写
def transac_lower():
    l = ['Hello','World','East','West','IBM','Apple']
    print([s.lower() for s in l])

# 把原子典的键值对颠倒并产生新的字典
def transac_dic ():
    dict1 = {"A":'a',"B":"b"}
    dict2 = {y:x for x,y in dict1.items()}
    print(dict1)
    print(dict2)

# 打印99乘法表
def print_multi():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d x %d = %d \t'%(i,j,i*j),end='')
        print()

# 替换列表中的值
def replace_list():
    num = ['hard','num',3,34,45,56,4,4,4,33,3,3,3,3,5654654,345353]
    print(num)
    for i in range(num.count(3)):
        ele_index = num.index(3)
        num[ele_index] = '3a'
    
    print(num)

if __name__=='__main__':
    print(lis)
    print(sortport(lis))
    print(power(2,130))
    print(calc([1,2,3]))
    print(fact(12))
    transac_lower()
    # filepath = r"F:\\my_project\\learn_python\\"
    # show_dir(filepath)
    # show_dir()
    # transac_dic()
    # print_multi()
    replace_list()
    