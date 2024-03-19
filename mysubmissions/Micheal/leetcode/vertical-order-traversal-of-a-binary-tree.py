# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dd = defaultdict(list)
        def traverse(root, level, height):
            if root == None:
                return None
            
            dd[level].append((root.val, height))
            print(root.val)
            l = traverse(root.left, level -1, height+1)

            r = traverse(root.right, level + 1, height+1)

            return dd
        ans = []
        val = (traverse(root,0,0)) 
        for key, value_list in val.items():
            val[key] = sorted(value_list, key=lambda x: (x[1], x[0]))

        print(val)
        mew = sorted(val)
        for j in range(len(mew)):
            sub = val[mew[j]]
            tmp = []
            for i in range(len(sub)):
                tmp.append(sub[i][0])
            ans.append(tmp)
        return ans



