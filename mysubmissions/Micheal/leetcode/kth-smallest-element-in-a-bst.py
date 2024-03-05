# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []



        def bst(root):
            if root == None:
                return []

            

            a = bst(root.left)

            b = bst(root.right)


            new = []
            
            new.extend(a)

            new.append(root.val)

            new.extend(b)

            return new
        ans = bst(root)
        return ans[k-1]


