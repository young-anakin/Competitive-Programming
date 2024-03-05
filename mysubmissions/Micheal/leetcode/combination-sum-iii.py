class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        tot = []

        bucket = []

        def backtrack(i):

            if len(bucket) == k and sum(bucket) == n:
                tot.append(bucket[::])
                return 
            if len(bucket) > k:
                return

            if i > 9:
                return

            if i not in bucket:
                bucket.append(i)
                backtrack(i)
                bucket.pop()
            backtrack(i+1)

        backtrack(1)

        return tot