class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = 0
        b = len(nums)-1
        count = 0
        while a < b:
            if nums[a] + nums[b] == k:
                count +=1
                a+=1
                b-=1
            elif nums[a] + nums[b] > k:
                b -=1
            elif nums[a] + nums[b] < k:
                a +=1
        return count
