from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cp = defaultdict(int)
        ans = 0
        a = 0
        b = 0
        while b <= len(fruits)-1:
            cp[fruits[b]] +=1
            while len(cp) > 2:
                cp[fruits[a]] -=1
                if cp[fruits[a]] == 0:
                    del cp[fruits[a]]
                a +=1
            ans = max(ans, b-a)
            b+=1
        return ans+1