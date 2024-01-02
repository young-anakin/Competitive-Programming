class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l = 0
        r = len(arr)-1
        while l < r:
            if arr[l] + arr[r] == target:
                return [l+1, r+1]
            elif arr[l] + arr[r] > target:
                r-=1
            elif arr[l] + arr[r] < target:
                l +=1
            