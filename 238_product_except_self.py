"""

https://leetcode.com/problems/product-of-array-except-self/

"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            if i-1 >= 0:
                left_prod *= nums[i-1]
            if len(nums)-i-1 < len(nums)-1:
                right_prod *= nums[len(nums) - i]
            answer[i] *= left_prod
            answer[len(nums)-i-1] *= right_prod
        return answer

print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))