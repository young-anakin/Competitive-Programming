# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        mx = max(nums)

        ind = nums.index(mx)

        def build(nums):
            if len(nums) == 0:
                return None
            
            mx = max(nums)
            ind = nums.index(mx)

            leaf = TreeNode(mx)
            
            l = build(nums[0:ind])
            r = build(nums[ind+1:])

            leaf.left = l
            leaf.right = r

            return leaf
        

        return build(nums)