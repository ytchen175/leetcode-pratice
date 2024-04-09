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
        old_to_new_dict = dict()
        
        def clone(node):
            if node in old_to_new_dict:
                return old_to_new_dict[node]
            else:
                new_node = Node(node.val)
                old_to_new_dict[node] = new_node
                
                for neighbor in node.neighbors:
                    new_node.neighbors.append(clone(neighbor))
                
                return new_node

        if node:
            return clone(node)
        else:
            return None
