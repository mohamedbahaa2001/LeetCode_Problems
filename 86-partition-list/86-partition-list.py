# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftPartition = []
        rightPartition = []
        thead = head
        while thead != None:
            if thead.val < x:
                leftPartition.append(thead.val)
            else:
                rightPartition.append(thead.val)
            thead = thead.next
            
        m = len(leftPartition)
        n = len(rightPartition)
        thead = head       
        for i in range( m ):
            thead.val = leftPartition[i]
            thead = thead.next
        for i in range(n ):
            thead.val = rightPartition[i]
            thead = thead.next
        return head