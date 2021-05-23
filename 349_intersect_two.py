"""

https://leetcode.com/problems/intersection-of-two-arrays/

"""
from typing import List
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        
        answer = []
        for n1 in nums1:
            i = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i and nums2[i] == n1:
                answer.append(n1)
        return answer

print(Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # 4 4 8 9 9
print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])) # 4 4 8 9 9