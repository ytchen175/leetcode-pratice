# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path, res):
            if not node:
                return
            else:
                path += str(node.val) # append node.val to the current path

                if (not node.left) and (not node.right): # if this node is a leaf node
                    res.append(path) # this path is vaild, append path into res  
                    return
                
                # there are still some nodes, add path + '->' and call recursively
                if node.left:
                    dfs(node.left, path + '->', res)
                if node.right:
                    dfs(node.right, path + '->', res)

        dfs(root, '', res)

        return res