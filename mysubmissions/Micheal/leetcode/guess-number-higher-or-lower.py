# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mx = n
        mn = 1

        md = (mx+mn) // 2

        while mx >= mn:
            md = (mx+mn) // 2
            val = guess(md)

            print(md)

            if val == 0:
                return md
            elif val == -1:
                mx = md - 1
            else:
                mn = md + 1
