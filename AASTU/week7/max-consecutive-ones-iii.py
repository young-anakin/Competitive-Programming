class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = 0
        zero = 0
        a = 0
        b = 0
        while b <= len(nums)-1:
            if nums[b] == 0:
                zero +=1
            if zero > k:
                if nums[a] == 0:
                    zero -=1
                a +=1
            b+=1
            maxx = max(maxx, (b+1) - a)
        return maxx-1
