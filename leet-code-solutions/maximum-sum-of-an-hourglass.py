from collections import defaultdict
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx = 0
        tot = 0
        for a in range(len(grid)-2):
            for b in range(len(grid[0])-2):
                # print("steve", (a,b))
                tot += sum(grid[a][b:b+3])
                tot += grid[a+1][b+1]
                tot += sum(grid[a+2][b:b+3])
                maxx = max(maxx, tot)
                tot = 0
            tot = 0
        return maxx