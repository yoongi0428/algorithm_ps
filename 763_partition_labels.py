"""

https://leetcode.com/problems/partition-labels/

"""
from typing import List
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