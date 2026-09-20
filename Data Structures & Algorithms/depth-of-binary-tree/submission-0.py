# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth=0
        self.max_depth=0
        def traverse(root):
            if root==None:
                return 
            self.depth+=1
            self.max_depth=max(self.max_depth,self.depth)
            traverse(root.left)
            traverse(root.right)
            self.depth-=1
        traverse(root)
        return self.max_depth


        