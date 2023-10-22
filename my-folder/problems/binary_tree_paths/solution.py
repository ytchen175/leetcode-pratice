# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        if not root:
            return
        
        def dfs(node, path, res):
            if not node:
                return
            else:
                path += str(node.val)
                
                if (not node.left) and (not node.right):
                    res.append(path)
                
                if node.left:
                    dfs(node.left, path + "->", res)
                if node.right:
                    dfs(node.right, path + "->", res)
        
        dfs(root, "", res)
                
        return res 