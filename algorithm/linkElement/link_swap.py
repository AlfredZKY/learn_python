class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairsRecursive(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # Nodes to be swaped 成对进行交换的
        first_node = head    # 1
        second_node = head.next # 2

        # swaping  # 成对进入 3 4 
        first_node.next = self.swapPairsRecursive(second_node.next)
        second_node.next = first_node

        return second_node

    def swapPairsIter(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
           first_node = head
           second_node = head.next

           # swaping 
           prev_node.next = second_node
           first_node.next = second_node.next
           second_node.next = first_node

           prev_node = first_node
           head = first_node.next
        return dummy.next

    def swapPairsStack(self, head: ListNode) -> ListNode: 
        if not (head and head.next):
            return head 
        p = ListNode(-1)
        cur,head,stack = head,p,[]
        while cur and cur.next:
            # 将前两个节点放入到栈中
            _,_ = stack.append(cur),stack.append(cur.next)

            # cur向前走两步
            cur = cur.next.next

            # 从stack中弹出元素，并用p连接
            p.next = stack.pop()
            p.next.next = stack.pop()

            # 把p移动到尾节点
            p = p.next.next
        # 如果链表是奇数
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next

    def printElement(self, head: ListNode) -> ListNode:
        while head != None:
            print(head.val,end='\t')
            head = head.next

     
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = None

# print(Solution().swapPairsRecursive(l1).val)
LinkElement = Solution()
# LinkElement.printElement(LinkElement.swapPairsRecursive(l1))
# LinkElement.printElement(LinkElement.swapPairsIter(l1))
LinkElement.printElement(LinkElement.swapPairsStack(l1))


