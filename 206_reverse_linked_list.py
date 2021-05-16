# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
            head
        p1 = p2 = reverseList(head.next)
        while p2.next:
            p2 = p2.next
        p2.next, head = head, None
        return p1