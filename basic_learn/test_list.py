 # 
 # Created by preference on 2020/04/28
 # Author: AlfredZKY
 # Files:test_list.py
 # WorkPlace:learn_python
 # 


list1 = ['Google','Runboob',1997,2000]
list2 = [1,2,2,3,4,5]


def list_Insert(nums):
    list2.insert(0,nums)


def update_List(index,nums):
    list2[index]=nums

def delete_Element(index):
    del list2[index]

def remove_Element(nums):
    list2.remove(nums)

def list_append(nums):
    list2.append(nums)

def pop_Element(nums):
    res = list2.pop(nums)
    return res

def reverse_list():
    list2.reverse()

def main():
    print(list1,list2)
    list_Insert(19)
    update_List(1,111)
    delete_Element(3)
    list_append(999)
    remove_Element(2)
    res = pop_Element(3)
    print(res)
    reverse_list()
    print(list1,list2)


if __name__ == '__main__':
    main()