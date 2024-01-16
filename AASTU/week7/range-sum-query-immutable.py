class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArray = [0]
        for ind in range(len(nums)):
            self.prefixArray.append(self.prefixArray[-1] + nums[ind])
        print(self.prefixArray)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixArray[right+1] - self.prefixArray[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)