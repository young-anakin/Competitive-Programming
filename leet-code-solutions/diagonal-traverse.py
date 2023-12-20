from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        div = defaultdict(list)
        for a in range(0, len(mat)):
            for b in range(0, len(mat[0])):
                div[a+b].append(mat[a][b])
        finalement = []
        for a, b in div.items():
            if a %2 == 0:
                finalement += reversed(b)
            else:
                finalement += b
        return finalement
                    
            
            