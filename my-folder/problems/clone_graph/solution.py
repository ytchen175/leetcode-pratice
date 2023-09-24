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
        old_to_new_hash_map = dict() # visited hash map, for old and new node mappings 

        def dfs(node):
            if node in old_to_new_hash_map: # have visited
                return old_to_new_hash_map[node] # return new one
            else:
                new_graph = Node(node.val) # copy old node.val
                old_to_new_hash_map[node] = new_graph # add mappings

                for neigh in node.neighbors:
                    new_graph.neighbors.append(dfs(neigh)) # search and append new node

                return new_graph

        # main
        if not node:
            return None
        else:
            return dfs(node)