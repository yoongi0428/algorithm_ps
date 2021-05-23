"""

https://leetcode.com/problems/min-stack/

"""

import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        

    def push(self, val: int) -> None:
        if len(self._stack) == 0 or val < self._stack[-1][1]:
            self._stack.append((val, val))
        else:        
            self._stack.append((val, self._stack[-1][1]))
        

    def pop(self) -> None:
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1][0]
        

    def getMin(self) -> int:
        return self._stack[-1][1]