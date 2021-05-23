"""

https://leetcode.com/problems/3sum/

"""
from typing import List
from collections import defaultdict, Counter

# Brute Force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        checker = defaultdict(list)
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans = sorted([nums[i], nums[j], nums[k]])
                        if not checker[tuple(ans)]:
                            checker[tuple(ans)] = True
                            answer.append(ans)
        return answer

# Two pointer
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer

nums = [-1,0,1,2,-1,-4]    # -1 1 1, -1, -1 ,2
print(Solution().threeSum(nums))
print(Solution2().threeSum(nums))