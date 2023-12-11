class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexes = {}
        for ind, val in enumerate(nums):
            indexes[val] = ind
        # print(indexes)
        for op in operations:
            nums[indexes[op[0]]] = op[1]
            indexes[op[1]] = indexes[op[0]]
            # print(nums)
            # indexes[indexes[1]]
        return nums