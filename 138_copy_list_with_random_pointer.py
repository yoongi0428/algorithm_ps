"""

https://leetcode.com/problems/copy-list-with-random-pointer/

"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next:Node = None, random:Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""
Leetcode solution 1. recursive approaches
- 결국, 모든 node를 clone하는 문제이고, 각 노드를 clone하는 것은 next, random을 clone하는 것이다.
- graph 관점의 해석, dfs, backtracking 인듯
- 이렇게 쉽게 생각하지 못한 이유는 문제를 어떻게 바라보고 정의할 것 인가를 먼저 생각안한 채 달려들었기 때문인듯 하다.
"""

class Solution:
    def __init__(self):
        self.hash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        if head in self.hash:
            return self.hash[head]
        
        new_node = Node(head.val, None, None)
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node
    
"""
Leetcode solution 2. iterative approaches
- 결국, 모든 node를 clone하는 문제이고, 각 노드를 clone하는 것은 next, random을 clone하는 것이다.
- solution 1을 iterative로 전환한 것
"""

class Solution:
    def __init__(self):
        self.hash = {}

    def getCloneNode(self, node):
        if node:
            if node not in self.hash:
                self.hash[node] = Node(node.val, None, None)
            return self.hash[node]
        else:
            return None
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        old_node = head
        new_node = Node(old_node.val, None, None)

        self.hash[old_node] = new_node

        while old_node is not None:
            new_node.next = self.getCloneNode(old_node.next)
            new_node.random = self.getCloneNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next

        return self.hash[head]

##########################################
#      MY naive brute force solution     #
##########################################
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        cur = head
        new_nodes = []
        id2index = {}
        idx = 0
        while cur is not None:
            id2index[id(cur)] = idx
            cur_new_node = Node(cur.val)
            if len(new_nodes) > 0:
                new_nodes[-1].next = cur_new_node
            new_nodes.append(cur_new_node)
            
            cur = cur.next
            idx += 1
        
        cur = head
        new_cur = new_nodes[0]
        while cur is not None:
            if cur.random:
                random_idx = id2index[id(cur.random)]
                new_cur.random = new_nodes[random_idx]

            cur, new_cur = cur.next, new_cur.next
        
        return new_nodes[0]