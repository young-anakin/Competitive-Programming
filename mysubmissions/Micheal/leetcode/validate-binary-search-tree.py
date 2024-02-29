# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root == None:
                return []
            a = check(root.left)
            b = check(root.right)
            arr = []
            arr.extend(a)
            arr.append(root.val)
            arr.extend(b)

            return arr
        arr = (check(root))
        new = []
        for ind in range(len(arr)):
            new.append(arr[ind])
        new.sort()
        for ind in range(len(new)-1):
            if new[ind] == new[ind+1]:
                return False
        if arr == new:
            return True
        return False

