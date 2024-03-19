# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def check(arr):
            if len(arr) == 0:
                return None
            
            md = arr[len(arr)//2]

            leaf = TreeNode(md)

            l = check(arr[0: len(arr)//2])

            r = check(arr[(len(arr)//2) + 1 :])

            leaf.left = l
            leaf.right = r

            return leaf
        
        return check(nums)
