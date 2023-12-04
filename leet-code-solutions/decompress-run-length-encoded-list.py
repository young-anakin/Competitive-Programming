class Solution(object):
    def decompressRLElist(self, nums):
        arr = []
        a = 0
        while a <= len(nums)-2:
            for b in range(0, (nums[a])):
                arr.append(nums[a+1])
            a+=2
        return (arr)
        