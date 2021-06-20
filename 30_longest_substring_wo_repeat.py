"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start, end = 0, 0
        ans = 0
        checker = defaultdict(int)
        for start in range(len(s)):
            end=start
            checker[s[end]] = 1
            while end < len(s) - 1 and checker[s[end+1]] == 0:
                end += 1
                checker[s[end]] = 1
            ans = max(ans, end - start + 1)
            checker = defaultdict(int)
        return ans

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))