class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_list = sorted(points, key=lambda x: x[0])
        maxx = 0
        for a in range(len(sorted_list)-1):
            maxx = max(maxx, sorted_list[a+1][0] - sorted_list[a][0])
        return maxx