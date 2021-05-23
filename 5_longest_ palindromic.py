"""
https://leetcode.com/problems/longest-palindromic-substring/
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