# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        node_depth = defaultdict(list)
        def traversal(root, dd, level):

            if root == None:
                return None
            
            dd[level].append(root.val)

            level +=1
            
            a = traversal(root.left, dd, level)

            b = traversal(root.right, dd, level)

            return dd

        ans = []
        # nodeHash = traversal(root, node_depth, 0)

        # print(traversal(root, node_depth, 0))

        dd = defaultdict(list)

        dd = traversal(root, node_depth, 0)

        if dd == None:
            return []
        for key, values in dd.items():
            if key%2 != 0:
                ans.append(values[::-1])
            else:
                ans.append(values)
        return ans

            

                