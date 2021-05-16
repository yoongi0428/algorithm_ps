"""
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         num_nodes = 0
#         cur_node = head
#         while cur_node:
#             num_nodes += 1
#             cur_node = cur_node.next
        
#         stack = []
#         cur_node = head
#         for _ in range(num_nodes // 2):
#             stack.append(cur_node.val)
#             cur_node = cur_node.next
        
#         if num_nodes % 2 == 1:
#             cur_node = cur_node.next
        
#         is_palindrome = True
#         for _ in range(num_nodes // 2):
#             val = stack.pop()
#             if val != cur_node.val:
#                 is_palindrome = False
#                 break
#             cur_node = cur_node.next
#         return is_palindrome

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next = slow, rev
            slow = slow.next
        
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        return not rev