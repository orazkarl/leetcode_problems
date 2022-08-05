# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = 0
        result_node = new_node = ListNode()
        while l1 or l2 or value:
            val1: int = 0
            val2: int = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            new_node.next = ListNode(value % 10)
            new_node = new_node.next
            value //= 10
        return result_node.next
        