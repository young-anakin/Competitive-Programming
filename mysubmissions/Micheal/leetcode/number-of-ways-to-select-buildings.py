class Solution:
    def numberOfWays(self, s: str) -> int:
        # Approach : in each iteration, count the number of 0's and 1's. If 
        zero = 0
        one = 0
        Count = defaultdict(int)
        ans = 0
        for ind in range(len(s)):
            if s[ind] == '0':
                zero +=1
                ans += Count['01']
                Count['10'] += one
            else:
                one +=1
                ans += Count['10']
                Count['01'] += zero
        return ans