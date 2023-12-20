class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for a in range(0, len(matrix)):
            for b in range(0, len(matrix)):
                if a == b:
                    break
                matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]
        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])
        
        