# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merger(root1, root2):

            if root1 == None and root2 == None:
                return None

            if root1 != None and root2 == None:
                return root1
            
            if root2 != None and root1 == None:
                return root2

            a = merger(root1.left, root2.left)

            b = merger(root1.right, root2.right)

            val = TreeNode(root1.val + root2.val)

            val.left = a
            val.right = b

            return val
        return merger(root1, root2)