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

if __name__ == '__main__':
    main()
