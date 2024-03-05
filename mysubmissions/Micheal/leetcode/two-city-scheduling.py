class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: -abs(x[0] - x[1]))
        n = len(costs)//2
        ans = 0
        A = B = n
        for cost in costs:
            if B == 0 or (cost[0] < cost[1] and A!=0):
                A-=1
                ans += cost[0]
            else:
                B-=1
                ans += cost[1]
        return ans
