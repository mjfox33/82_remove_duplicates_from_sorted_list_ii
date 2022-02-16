from dataclasses import dataclass
from dataclasses import dataclass
# Definition for singly-linked list.
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0,head)
        predecessor = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                predecessor.next = head.next
            else:
                predecessor = predecessor.next
            head = head.next
        return sentinel.next