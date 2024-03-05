# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        # mn, mx, diff
        def check(root):
            
            if root == None:
                return None

            a = check(root.left)

            b = check(root.right)


            if a == None:
                a = (root.val, root.val, 0)

            
            if b == None:
                b =  (root.val, root.val, 0)

                


            ans = max(abs(a[0] - root.val), abs(a[1] - root.val))

            val = (min(a[0], root.val), max(a[1], root.val), max(ans, a[2]))


            ans2 =  max(abs(b[0] - root.val), abs(b[1] - root.val))

            val1 = (min(b[0], root.val), max(b[1], root.val), max(ans2, b[2]))

            return (min(val[0], val1[0]), max(val[1], val1[1]), max(val[2], val1[2]))
        x = check(root)
        return x[2]