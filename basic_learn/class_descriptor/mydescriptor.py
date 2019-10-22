class name_des(object):
    def __init__(self):
        self.__name = None
    
    def __get__(self,instance,owner):
        print('call __get__')
        return self.__name

    def __set__(self,instance,value):
        print('call __set__')
        if isinstance(value,str):
            self.__name = value
        else:
            raise TypeError("Must be an string")

class normal(object):
    def __init__(self,name):
        self.name = name

class test(object):
    name = name_des()

class test1(object):
    name = normal("")


class Score:
    def __init__(self,default):
        self._score = default
    
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError("Valid value must be in [0,100]")
        self._score = value

    def __get__(self,instance,owner):
        return self._score

    def __del__(self):
        del self._score

class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self,name,math,chinese,english):
        self.name=name
        self.math=math
        self.chinese = chinese
        self.english = english
    
    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(self.name,\
            self.math,self.chinese,self.english)

def main():
    t = test()
    print(t.name)
    # 赋值给数字就会报错
    # t.name = 3
    t.name = "my name is zky"
    print(t.name)

    print("-------------------------------")
    t1 = test1()
    print(t1.name)
    t1.name = 3
    print(t1.name)

    print("++++++++++++++++++++++++++++++")
    std1 = Student('小明',7,837,68)
    print(std1)
    std2 = Student('小明','76','87','68')
    print(std2)
if __name__ == '__main__':
    main()
