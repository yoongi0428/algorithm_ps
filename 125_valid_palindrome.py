"""

https://leetcode.com/problems/valid-palindrome/

"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))