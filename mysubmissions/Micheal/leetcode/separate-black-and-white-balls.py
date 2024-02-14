class Solution:
    def minimumSteps(self, s: str) -> int:
        lst = len(s)-1

        cp = 0
        zero = 0
        while lst >= 0:
            if s[lst] == "0":
                zero +=1
            else:
                cp += zero
            lst -=1
        return cp


        