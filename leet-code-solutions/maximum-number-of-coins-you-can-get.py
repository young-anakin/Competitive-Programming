class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        count = int(len(piles) / 3)
        iterVal = 0
        a = 0
        summ = 0
        while iterVal != count:
            a+=1
            summ += piles[a]
            iterVal += 1
            a+=1
        return summ
            
            