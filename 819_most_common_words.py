"""

https://leetcode.com/problems/most-common-word/

"""
from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        counter = Counter(paragraph.lower().split())

        for b in banned:
            del counter[b]
        return counter.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution().mostCommonWord(paragraph, banned))