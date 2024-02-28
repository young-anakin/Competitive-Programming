# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def calc(l, r):
            if l == None and r == None:
                return True

            if (l == None and r != None) or ( l != None and r == None) :
                return False


            a = calc(l.left , r.right)

            b = calc(l.right, r.left)


            print(a,b)

            
            if l.val == r.val:
                return True and a and b
            return False and b and a

        

        return calc(root.left, root.right)
            

            


            



