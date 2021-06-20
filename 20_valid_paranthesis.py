"""

https://leetcode.com/problems/valid-parentheses/

"""
from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {']': '[', '}': '{', ')':'('}
        def is_open(c):
            return c in ['(', '{', '[']

        ans = True
        for c in s:
            if is_open(c):
                stack.append(c)
            else:
                if len(stack) <= 0 or stack[-1] != close_to_open[c]:
                    ans = False
                    break
                stack.pop()
        
        num_remains = len(stack)
        if num_remains > 0:
            ans = False
        
        return ans

print(Solution().isValid('{[]}'))
print(Solution().isValid('[]'))
print(Solution().isValid('()'))
print(Solution().isValid('([)]'))