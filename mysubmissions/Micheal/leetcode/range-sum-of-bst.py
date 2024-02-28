# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        
        x = self.rangeSumBST(root.left, low, high)

        y = self.rangeSumBST(root.right, low, high)

        ans = 0

        z = root.val 
        if z >= low and z <= high:
            return x + y + z
        else:
            return x + y

        
