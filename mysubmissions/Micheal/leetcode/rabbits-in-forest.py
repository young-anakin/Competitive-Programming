class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        identical = defaultdict(int)
        ans = 0
        for ind in range(len(answers)):
            if identical[answers[ind]] == 0:
                ans += answers[ind] + 1
                identical[answers[ind]] += answers[ind]
            else:
                identical[answers[ind]] -=1
        return ans