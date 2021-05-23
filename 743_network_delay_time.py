"""

https://leetcode.com/problems/network-delay-time/


"""
import sys
from typing import List
from collections import defaultdict
from queue import PriorityQueue
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        Q = [(0, k)]
        dist = defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) != n:
            return -1
        return max(dist.values())

print(Solution().networkDelayTime(times=[[3,1,5],[2,3,1],[3,4,1]], n = 8, k = 3))