class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        tot = []

        bucket = []
        def backtrack(i):
            if i >= len(nums):
                xz = bucket[::]
                xz.sort()
                if xz not in tot:
                    tot.append(xz[::])
                return 


            
            bucket.append(nums[i])

            backtrack(i+1)
            
            bucket.pop()

            backtrack(i+1)
        backtrack(0)
        return tot
