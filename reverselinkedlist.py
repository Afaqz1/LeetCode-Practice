class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self, head: listNode) -> listNode:
        """prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev"""
        if not head:
             return None
         
        newHead = head
        if head.next:
            newHead = self.reverseLinkedList(head.next)
            head.next.next = head
        head.next = None

        return newHead