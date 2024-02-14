from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print("It works")
        arry1 = [i for i in l1.val]
        arry2 = [i for i in l1.val]
        print(arry1)
        print(l2)

obj = Solution()

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

l1 = list_to_linked_list([1, 2, 3])
l2 = list_to_linked_list([4, 5, 6])


obj.addTwoNumbers(l1, l2)
