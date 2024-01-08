class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Approach : We sort the array and then we first choose two indices from left and one from right and substitute the minimum value of their sum
        nums.sort()
        a = 0
        b = 1
        c = len(nums)-1
        ms = 0
        ans = 20000
        minSum = 100000
        for ind in range(len(nums)-2):
            l = ind +1 
            r = len(nums)-1
            while l < r:
                s = nums[ind] + nums[l] + nums[r]
                ms = abs(s - target)
                if ms < minSum:
                    minSum = ms
                    ans = s
                if s < target:
                    l +=1
                elif s > target:
                    r -=1
                else:
                    return s
        return ans
