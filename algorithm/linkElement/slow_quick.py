class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return head
        
        slow = head
        quick = head
        while quick and slow:
            # 这里因为quicl跳两次，所以要判断quick和quick.next是否都为空 否则会报出NoneType的异常
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False
            if quick is slow:
                print(quick,slow)
                return True
        return False

    def Print(self,head:ListNode):
        i = 0
        while head :
            if i > 6:
                break
            print(head.val,end='\t')
            head= head.next
            i += 1

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

linkEle = Solution()
# linkEle.Print(l1)
print(linkEle.hasCycle(l1))

