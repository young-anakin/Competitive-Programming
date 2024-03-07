class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ind in range(len(matrix)):
            val = bisect_left(matrix[ind], target)
            if val >= len(matrix[ind]):
                continue
            if matrix[ind][val] == target:
                return True
        
        return False