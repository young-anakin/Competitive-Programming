class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        mstack = []
        currMin = float("inf")

        for ind in range(len(nums)):
            while mstack and mstack[-1][0] <= nums[ind]:
                mstack.pop()
            
            if mstack and nums[ind] > mstack[-1][1]:
                return True
            

            currMin = min(currMin, nums[ind])
            mstack.append((nums[ind], currMin))

        return False



