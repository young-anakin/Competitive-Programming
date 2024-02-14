class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        whole = Counter(nums)
    
        n = len(whole)
        cp = 0
        print(n)
        for ind in range(len(nums)):
            checker = defaultdict(int)
            for j in range(ind, len(nums)):
                checker[nums[j]] +=1
                if len(checker) == n:
                    cp +=1
        return cp