# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        # In-order traversal of Tree
        def sorter(root):
            if not(root):
                return []
            
            sub = []
            l = sorter(root.left)
            r = sorter(root.right)

            sub.extend(l)
            sub.append(root.val)
            sub.extend(r)

            return sub
        # Construct a normal binary search tree from sorted tree
        def con(arr):
            if len(arr) == 0:
                return None
            vl = arr[len(arr)//2]
            root = TreeNode(vl)

            l = con(arr[0:len(arr)//2])
            r = con(arr[(len(arr)//2) + 1 : ])

            root.left = l
            root.right = r

            return root
        arr = sorter(root)

        return con(arr)