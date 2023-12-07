class Solution:
    def totalMoney(self, n: int) -> int:
        r = n % 7
        v = n // 7
        ans = v * (28) + (v * (v - 1) // 2) * 7
        ans += (r * (r + 1) // 2) + r * (v)
        return ans
                                
            