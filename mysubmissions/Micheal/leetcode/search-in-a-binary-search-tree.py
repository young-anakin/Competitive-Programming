# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = []
        if root == None:
            return 

        a = self.searchBST(root.left, val)
        b = self.searchBST(root.right, val)

        if a != None:
            return a
        if b != None:
            return b
        if root.val == val:
            ans.append(root.val)
            return root

