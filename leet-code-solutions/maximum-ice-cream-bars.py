class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        a = 0
        summ = 0
        for ind in range(len(costs)):
            summ += costs[ind]
            a+=1
            if summ == coins:
                break
            elif summ > coins:
                summ - costs[ind]
                a-=1
                break
        return a