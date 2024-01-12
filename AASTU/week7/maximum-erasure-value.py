class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a = 0
        b = 0
        summ = 0
        maxx = 0
        cp = defaultdict(int)
        while b <= len(nums)-1:
            cp[nums[b]] +=1
            while cp[nums[b]] > 1:
                cp[nums[a]] -=1
                summ -= nums[a]
                a +=1
            summ += nums[b]            
            maxx = max(summ, maxx)
            b +=1
        return maxx
