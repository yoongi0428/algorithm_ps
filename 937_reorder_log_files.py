"""

https://leetcode.com/problems/reorder-data-in-log-files/

"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
            print(log.split()[1])
        letters = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))