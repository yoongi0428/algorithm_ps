"""

https://leetcode.com/problems/number-of-islands/

"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(x, y, nr, nc):
            if 0 <= x and x < nr and 0 <= y and y < nc:
                return True
            return False
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        discovered = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        queue = []
        answer = 0
        # BFS
        for i in range(num_rows):
            for j in range(num_cols):
                if discovered[i][j] or grid[i][j] == '0':
                    continue
                queue = [(i, j)]
                answer += 1
                while len(queue) > 0:
                    x, y = queue[0]
                    queue = queue[1:]
                    if discovered[x][y]:
                        continue
                    discovered[x][y] = 1
                    
                    if is_valid(x-1, y, num_rows, num_cols) and grid[x-1][y] == '1':
                        queue.append((x-1, y))
                    if is_valid(x+1, y, num_rows, num_cols) and grid[x+1][y] == '1':
                        queue.append((x+1, y))
                    if is_valid(x, y-1, num_rows, num_cols) and grid[x][y-1] == '1':
                        queue.append((x, y-1))
                    if is_valid(x, y+1, num_rows, num_cols) and grid[x][y+1] == '1':
                        queue.append((x, y+1))

        return answer

grid = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]]

print(Solution().numIslands(grid))