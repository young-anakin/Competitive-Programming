class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_arr = []
        cp = 0
        orig = 0
        a = len(nums)-1
        nums.append('a')
        while nums[orig] != 'a':
            if nums[orig] == val:
                nums.pop(orig)
                continue
            else:
                cp +=1
            orig +=1
        nums.pop(-1)
        return cp
            