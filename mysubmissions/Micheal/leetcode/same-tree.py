# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if p == None and q == None:
                return True
            if (p == None and q != None) or (p != None and q == None):
                return False

            a = check(p.left, q.left)

            b = check(p.right, q.right)

            if p.val == q.val:
                return True and a and b

        return check(p, q)  