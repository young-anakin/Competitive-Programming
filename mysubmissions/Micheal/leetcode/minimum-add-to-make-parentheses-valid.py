class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        rem = 0
        op = 0
        for ind in range(len(s)):
            if s[ind] == '(':
                op +=1
            else:
                if op != 0:
                    op -=1
                else:
                    rem +=1
        return rem + op