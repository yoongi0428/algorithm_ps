"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        checker = defaultdict(int)

        for n in nums:
            checker[n] += 1
        
        return [i for i in range(1, N+1) if checker[i] == 0]