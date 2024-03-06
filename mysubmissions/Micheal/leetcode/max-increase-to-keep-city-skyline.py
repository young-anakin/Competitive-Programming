class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        RowMax = []
        ColMax = []
        newSkyline = []
        for ind in range(len(grid)):
            RowMax.append(max(grid[ind]))
        
        rez = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        for ind in range(len(rez)):
            ColMax.append(max(rez[ind]))
        

        # [8, 7, 9, 3] [9, 4, 8, 7]

        for ind in range(len(grid)):
            innerSkyline = []
            for j in range(len(grid)):
                innerSkyline.append(min(ColMax[j], RowMax[ind]))
            newSkyline.append(innerSkyline)
        ans = 0
        for ind in range(len(grid)):
            for j in range(len(grid)):
                ans += newSkyline[ind][j] - grid[ind][j]
        return ans
        


                