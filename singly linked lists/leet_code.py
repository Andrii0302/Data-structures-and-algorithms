class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head
        
        while current_node:
            if current_node.val == val:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                prev_node = current_node
                current_node = current_node.next

        return dummy.next
