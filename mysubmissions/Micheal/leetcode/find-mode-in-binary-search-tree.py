# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        mode = defaultdict(int)


        def check(root, dd):
            if root == None:
                ab = {}
                return 
            l = check(root.left, dd)
            r = check(root.right, dd)
            dd[root.val] +=1
            return dd
        ans = []

        sep = check(root, mode)
        mx = 0
        for values in sep.values():
            mx = max(mx, values)
        new = defaultdict(int)
        for key, values in check(root, new).items():
            print(key, values)
            if mx == values:
                ans.append(key)
        return ans
