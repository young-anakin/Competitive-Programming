class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for a in range(len(mat)):
            for b in range(len(mat)):
                if a == b:
                    summ += mat[a][b]
        for a in range(len(mat)):
            for  b in range(len(mat)):
                if a+b == len(mat)-1:
                    summ += mat[a][b]
        if len(mat) %2 == 1:
            summ -= mat[len(mat)//2][len(mat)//2]
        return summ