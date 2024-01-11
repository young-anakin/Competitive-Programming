class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        ans = 0
        maxx = 0
        b = 0
        a = 0
        while b <= len(nums)-1:
            if nums[b] == 0:
                zeroCount +=1
            while zeroCount > 1:
                if nums[a] == 1:
                    ans -=1
                else:
                    ans -=1
                    zeroCount -=1
                a +=1
            b+=1
            ans +=1
            maxx = max(ans, maxx)
        return maxx -1
            
            
            