# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = []
        mxDepth = 0
        dd = defaultdict(list)
        def check(node, height, k):
            if node == None:
                return None
            
            dd[height].append(k)

            check(node.left, height+1, 2*k)
            check(node.right, height+1, (2*k)+1)
        


        ans = check(root, 0, 1)
        mx = 0
        for key, values in dd.items():
            mx = max(mx, max(dd[key]) - min(dd[key]))
        return mx+1