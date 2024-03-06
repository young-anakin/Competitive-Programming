class Solution:
    def mySqrt(self, x: int) -> int:
        mn = 1
        mx = x

        while True:
            md = (mn + mx) //2

            if md ** 2 <= x and (md+1) ** 2 > x:
                return md

            elif md ** 2 > x and (md+1) ** 2 > x:
                mx = md -1
                
            else:
                mn = md + 1