import copy

def test():
    x =[1]
    x.append(x)
    y = copy.deepcopy(x)
    print(x == y)

def main():
    print("hello world")
    l1 = [[1,2],(30,40)]
    l2 = copy.deepcopy(l1)
    print(l1 == l2,l1 is l2)

    a = [3]
    b = a
    print(a,b)
    print(a == b,a is b)
    a.append(4)
    print(a,b)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)

if __name__ == '__main__':
    main()
    #test()