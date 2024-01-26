class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for ind in range(len(nums))]
        summ = 1
        zero = False
        for ind in range(len(nums)):
            if nums[ind] == 0:
                zero = True
                continue
            summ *= nums[ind]
        ans = []
        if zero == True:
            for ind in range(len(nums)):
                if nums[ind] == 0:
                    ans.append(summ)
                    continue
                ans.append(0)
            return ans
        for ind in range(len(nums)):
            ans.append(int(summ//nums[ind]))
        return ans
        print(summ)