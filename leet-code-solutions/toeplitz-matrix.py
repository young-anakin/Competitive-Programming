class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for a in range(0, len(matrix)):
            for b in range(0, len(matrix[a])):
                if a-1 < 0 or b-1 < 0:
                    continue
                else:
                    if matrix[a][b] != matrix[a-1][b-1]:
                        return False
        return True
            
        