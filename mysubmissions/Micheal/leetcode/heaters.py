class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        mx = 0

        heaters.sort()
        heaters.append(10000000000000)
        for ind in range(len(houses)):
            val = bisect_left(heaters, houses[ind])
            temp = min(abs(heaters[val] - houses[ind]), abs(houses[ind] - heaters[val-1]))
            mx = max(mx, temp)
        return mx