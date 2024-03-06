class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn = 0
        mx = len(nums)-1

        # if len(nums) == 1:
        #     return nums[0]
        while mn < mx:
            md = (mn+mx)//2 

            if nums[md] < nums[mn]:
                mx = md
            elif nums[md] > nums[mx]:
                mn = md + 1
            else:
                return nums[mn]
        return min(nums[mn], nums[mx])
