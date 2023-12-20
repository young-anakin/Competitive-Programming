class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix  =[]
        for a in range(len(matrix[0])):
            sub = []
            for b in range(len(matrix)):
                sub.append(matrix[b][a])
            new_matrix.append(sub)
        return new_matrix