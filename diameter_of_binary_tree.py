# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0] #using a list but just going to use elecment 0 of this list
        def dfs(root): 
            if root is None: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            diameter[0] = max(left + right, diameter[0])
            
            return max(left, right) + 1
            
                    
        # diameter = 0
        dfs(root)
        return diameter[0]
