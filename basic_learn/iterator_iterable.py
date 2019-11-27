class s:
    def __init__(self,x):
        self.x=x    #获取传入的对象
        self.index=0#维护索引值
    
    def __next__(self):
        try:
            result = self.x[self.index]# 获取传入对象的值
        except IndexError:
            raise StopIteration # 如果索引值错误，则抛出异常
        self.index +=1  #索引值+1，用来获取传入对象的下一个值
        return result   #返回传入对象的值
    
    def __iter__(self):
        return self

class s1:
    def __init__(self,x):
        self.x=x    #获取传入的对象
        self.index=0#维护索引值
    
    def __next__(self):
        try:
            result = self.x[self.index]# 获取传入对象的值
        except IndexError:
            raise StopIteration # 如果索引值错误，则抛出异常
        self.index +=1  #索引值+1，用来获取传入对象的下一个值
        return result   #返回传入对象的值

class b:
    def __init__(self,x):
        self.x = x
    
    def __iter__(self):
        return s(self.x)

if __name__ == "__main__":
    # TypeError: 's1' object is not iterable
    # a = s1([1,2,3])
    a = b([1,2,3])
    for x in a:
        print(x)
    print('-----------------------------')

    a = s([1,2,3])
    print(next(a))
    for x in a:
        print(x)
    print('-----------------------------')
    # a对象还是属于迭代器对象，因为在next获取下一个值会报错
    # print(next(a))