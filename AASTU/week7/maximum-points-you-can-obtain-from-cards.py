class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxx = 0
        summ = 0
        prefix = sum(cardPoints)
        for ind in range(len(cardPoints)-k):
            summ += cardPoints[ind]
        maxx = prefix - summ
        print(prefix, summ)
        a = 0
        b = len(cardPoints)-k
        # while b<= len(cardPoints)-1:
        #     summ -= cardPoints[a]
        #     summ += cardPoints[b]
        #     print(cardPoints[a], cardPoints[b])
        #     print(summ)
        #     a+=1
        #     b+=1
        while b <= len(cardPoints)-1:
            summ -= cardPoints[a]
            summ += cardPoints[b]
            maxx = max(maxx, prefix-summ)
            print(cardPoints[a], cardPoints[b])
            print(prefix, summ,  prefix-summ)
            a +=1
            b +=1
        return maxx
        
            