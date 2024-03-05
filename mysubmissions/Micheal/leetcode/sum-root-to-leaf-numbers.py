# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        arr = []
        def splitter(root):
            if root == None:
                return []
            

            a = splitter(root.left)
            
            b = splitter(root.right)

            if a == [] and b == []:
                return [str(root.val)]

            new = []
            for ind in range(len(a)):
                new.append(str(root.val) + a[ind])
            for ind in range(len(b)):
                new.append(str(root.val) + b[ind])
            
            return new
        xz = splitter(root)
        ans = 0
        print(xz)
        for ind in range(len(xz)):
            print(xz[ind])
            ans += int(xz[ind])

        return ans            








            
            




