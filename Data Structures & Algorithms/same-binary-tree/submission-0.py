# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res=True
        def dfs(p,q):
            if (p is None and q is not None) or (q is None and p is not None):
                self.res=False
                return
            if p and q and p.val != q.val:
                self.res=False
                return 
            if p and q and p.val == q.val: 
                dfs(p.left,q.left)
                dfs(p.right,q.right)
        dfs(p,q)
        return self.res

        
        