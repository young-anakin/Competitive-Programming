class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)

        mn = 1

        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        # if 
        def checker(mn, mx, hours):
            md = (mn + mx) // 2
            while mx > mn:
                md = (mn + mx) // 2
            
                cp = 0

                for ind in range(len(piles)):
                    cp += math.ceil(piles[ind]/md)

                if cp <= h:
                    mx = md
                elif cp > h:
                    mn = md +1
            return mn

        x = checker(mn, mx, h)
        return x    
