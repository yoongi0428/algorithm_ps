"""

https://leetcode.com/problems/reverse-linked-list/

"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
            head
        p1 = p2 = reverseList(head.next)
        while p2.next:
            p2 = p2.next
        p2.next, head = head, None
        return p1