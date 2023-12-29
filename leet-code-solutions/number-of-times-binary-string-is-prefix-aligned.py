class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        prefix = [0]
        for a in range(n):
            prefix.append(prefix[-1] + a+1)
        prefix.pop(0)
        print(prefix)
        count = 0
        summ = 0
        for a in range(n):
            summ += flips[a]
            if summ == prefix[a]:
                count +=1
        return(count)
            
        # for a in range()