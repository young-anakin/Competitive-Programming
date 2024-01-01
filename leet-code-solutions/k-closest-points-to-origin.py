from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        finalement = []
        ansDict = defaultdict(list)
        for point in points:
            ans = math.sqrt((0-point[0])**2 + (0-point[1])**2) 
            ansDict[ans].append(point)
            finalement.append(ans)

        finalement = set(finalement)
        finalement = list(finalement)
        finalement.sort()
        ans = []
        a = 0
        for a in range(len(finalement)):
            ans += ansDict[finalement[a]]
                 
        print(ansDict)
        print(finalement)
        return(ans[0:k])