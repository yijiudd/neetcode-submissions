# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res=False

        def dfs(root):
            if root is None:
                return 
            if root.val == subRoot.val and compare(root,subRoot):
                self.res=True
                return
            dfs(root.left)
            dfs(root.right)
        def compare(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val !=q.val:
                return False
            return compare(p.left,q.left) and compare(p.right,q.right)

        dfs(root)
        return self.res