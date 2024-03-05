class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        bucket = []

        def backtrack(i):
            if sum(bucket) == target:
                final.append(bucket[::])
                return
            if sum(bucket) > target or i >= len(candidates):
                return
            
            
            
            if sum(bucket) < target:
                bucket.append(candidates[i])
                backtrack(i)
                bucket.pop()
                backtrack(i+1)
        backtrack(0)

        return final