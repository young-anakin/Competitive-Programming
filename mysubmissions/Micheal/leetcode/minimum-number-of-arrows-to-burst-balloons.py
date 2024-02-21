class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])

        curr = points[0]
        cp = 1
        for ind in range(1, len(points)):
            if curr[1] >= points[ind][0]:
                continue
            else:
                cp +=1
                curr = points[ind]
        return cp