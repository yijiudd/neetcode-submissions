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
            dfs(root.left)
            dfs(root.right)
        def compare(p,q):
            if p is None and q is None:
                return True
            if (q is None and p is not None) or (q is not None and p is None):
                return False
            if p !=None and q!=None and p.val !=q.val:
                return False
            if p !=None and q!=None and p.val==q.val:
                return compare(p.left,q.left) and compare(p.right,q.right)

        dfs(root)
        return self.res