class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nexts = 100000000
        maxs = 1000000000
        prev = -100000000
        for a in range(0, len(nums)-1):
            if nums[a] > nums[a+1]:
                if nexts >= prev:
                    nums.pop(a)
                else:
                    nums.pop(a+1)
                break
            prev = nums[a]
            if a == len(nums)-2:
                nexts = maxs
            else:
                nexts = nums[a+2]
        for a in range(0, len(nums)-1):
            if nums[a] > nums[a+1]:
                return False
        return True
        
#         chance = 1
#         if nums[0] <= nums[1]:
#             for i in range(0, len(nums)-1):
#                 if nums[i] > nums[i+1]:
#                     chance -= 1
#                 if chance < 0:
#                     return False
#         else:
#             for i in range(1, len(nums)-1):
#                 if nums[i] > nums[i+1]:
#                     chance -=1 
#                 if chance <= 0:
#                     return False
                
#         return True