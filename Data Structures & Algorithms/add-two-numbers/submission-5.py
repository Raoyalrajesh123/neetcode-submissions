# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy
        carry=0
        while l1 or l2 or carry:
            if l1 is not None:
                x=l1.val
            else:
                x=0
            if l2 is not None:
                y=l2.val
            else:
                y=0
            sum1=x+y+carry
            sum=sum1%10
            carry=sum1//10
            curr=ListNode(sum)
            temp.next=curr
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            temp=temp.next
            curr=0
        return dummy.next