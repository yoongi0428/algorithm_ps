from typing import List

"""
https://leetcode.com/problems/partition-labels/

A string s of lowercase English letters is given. 
We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


Note:

s will have length in range [1, 500].
s will consist of lowercase English letters ('a' to 'z') only.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left_right = {}
        for i, c in enumerate(s):
            if c not in left_right:
                left_right[c] = (i, i)
            else:
                left, right = left_right[c]
                left_right[c] = (left, i)
        left_right = sorted(left_right.values(), key=lambda x: x[0])

        ans = []
        cur_left, cur_right = -1, -1
        for l, r in left_right:
            if cur_left == -1 and cur_right == -1:
                cur_left, cur_right = l, r
            elif l < cur_right:
                cur_right = max(cur_right, r)
                cur_left = min(cur_left, l)
            else:
                length = cur_right - cur_left + 1
                ans.append(length)
                
                cur_left = l
                cur_right = r
        length = cur_right - cur_left + 1
        ans.append(length)
        return ans

if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))