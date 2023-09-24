"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new_hash_map = dict()

        def dfs(node):
            if node in old_to_new_hash_map:
                return old_to_new_hash_map[node]

            new_graph = Node(node.val)
            old_to_new_hash_map[node] = new_graph

            for neigh in node.neighbors:
                new_graph.neighbors.append(dfs(neigh))

            return new_graph

        if not node:
            return None
        else:
            return dfs(node)