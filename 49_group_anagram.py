"""

https://leetcode.com/problems/group-anagrams/

"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        idx_dict = {}
        answer = []
        # for each word
        for string in strs:
            # sort alphabetical order
            sorted_string = ''.join(sorted(string))
            # get index from dictionary
            if sorted_string not in idx_dict:
                idx_dict[sorted_string] = len(idx_dict)
                answer.insert(len(idx_dict), [])
            idx = idx_dict.get(sorted_string, len(idx_dict))
            answer[idx].append(string)
        return answer


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))