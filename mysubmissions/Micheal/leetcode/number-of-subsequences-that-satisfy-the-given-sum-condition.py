class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt=0
        mod=10**9+7
        print(nums, len(nums))
        nums.sort()

        for i,n in enumerate(nums):
            x=target-n
            if x<n:
                break
            idx=bisect_right(nums,x)

            idx -=1
            cnt+= (pow(2,abs(idx-i), mod))
        cnt = cnt % mod
        return cnt
        