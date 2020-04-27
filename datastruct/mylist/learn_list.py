
class node(object):
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.cargo)

class Node(object):
    def __init__(self,initdata):
        self.__data = initdata
        self.__next = None
    
    def __str__(self):
        return self.__data

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next
    
    def setData(self,newData):
        self.__data = newData
    
    def setNext(self,newNext):
        self.__next = newNext

class SinCycLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    # def __len__(self):
    #     # 输出头节点，返回链表的长度
    #     curr = self.head
    #     counter = 0
    #     while curr is not None:
    #         counter += 1
    #         curr = curr.next
    #     return counter
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self,item):
        prev = self.head
        while prev.getNext() != self.head:
            curr = prev.getNext()
            if curr.getData() == item :
                prev.setNext(prev.getNext())
            prev = prev.getNext()
    
    def search(self,item):
        prev = self.head
        while prev.getNext() != self.head:
            curr = prev.getNext
            if curr.getData() == item:
                return True
            prev = prev.getNext()
       
    def empty(self):
        return self.head.getNext() == self.head

    def size(self):
        count = 0
        curr = self.head.getNext()
        while curr != self.head:
            count += 1
            curr = curr.getNext()
        return count

    def traveseList(self):
        res = []
        prev = self.head
        while prev.getNext() != self.head:
            if prev.getData() != None:
                res.append(prev.getData())
            prev = prev.getNext()
        return res

# print(node("text"))

# 定义节点
node1 = node("one")
node2 = node("two")
node3 = node("third")

node1.next = node2
node2.next = node3


def printList(node):
    while node:
        print(node)
        node = node.next


# 使用递归的方法打印
def printBackward(lists):
    if lists == None:
        return
    
    printBackward(lists.next)
    print(lists)

def useSineLinkedList():
    s = SinCycLinkedList()
    print('s.empty() == %s, \t s.size() == %s' % (s.empty(),s.size()))

    s.add(1)
    s.add(11)
    s.add(111)
    s.add(1111)

    print('s.empty() == %s, \t s.size() == %s' % (s.empty(),s.size()))
    print(s.traveseList())

def main():
    # printList(node1)
    # printBackward(node1)
    useSineLinkedList()


if __name__ == '__main__':
    main()