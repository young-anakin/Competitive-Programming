class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #for counting F's
        a = 0
        b = 0
        zero = 0
        cp = 0
        maxx = 0
        while b <= len(answerKey)-1:
            if answerKey[b] == "F":
                zero +=1
            while zero > k:
                if answerKey[a] == "F":
                    zero -=1
                a +=1
                cp -=1
            cp +=1
            b +=1
            maxx = max(maxx, cp)
        

        #for coutning T's
        a = 0
        b = 0
        zero = 0
        cp = 0
        while b <= len(answerKey)-1:
            if answerKey[b] == "T":
                zero +=1
            while zero > k:
                if answerKey[a] == "T":
                    zero -=1
                a +=1
                cp -=1
            cp +=1
            b +=1
            maxx = max(maxx, cp)
        return  maxx