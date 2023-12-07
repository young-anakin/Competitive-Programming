class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        pivotList = []
        count = 0
        for a in range(0, len(nums)):
            if nums[a] < pivot:
                before.append(nums[a])
            elif nums[a]  == pivot:
                pivotList.append(pivot)
            else:
                after.append(nums[a])

        return before + pivotList + after