"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
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