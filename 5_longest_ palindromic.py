"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # exception: length 1
        if len(s) == 1 or s == s[::-1]:
            return s
        
        def expand(s, left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1: right-1]
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(s, i, i+1), expand(s, i, i+2), key=len)
        return result

# print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
# print(Solution().longestPalindrome('ac'))
# print(Solution().longestPalindrome('a'))