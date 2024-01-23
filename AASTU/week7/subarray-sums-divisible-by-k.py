class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Approach : 
        
        prefix = [nums[0]]
        checker = defaultdict(int)
        checker[0] = 1
        #calculating prefix for nums array
        for ind in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[ind])
        
        ans = 0
        for ind in range(len(nums)):
            ans += checker[prefix[ind]%k]
            checker[prefix[ind] %k] +=1
        return ans
        