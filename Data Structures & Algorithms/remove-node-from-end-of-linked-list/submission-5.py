# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        count1=0
        if temp.next is None:
            return None
        while temp is not None:
            count1+=1
            temp=temp.next
        z=count1-n
        temp=head
        if count1==n:
            return temp.next
        while temp is not None:
            if count==z-1 and temp.next is not None:
                temp.next=temp.next.next
            elif count==z-1 and temp.next is None:
                temp.next=None   
            temp=temp.next
            count+=1
        return head