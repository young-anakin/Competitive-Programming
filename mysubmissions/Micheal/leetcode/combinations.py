class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        bucket = []

        def answer(val):
            if len(bucket) == k:
                ans.append(bucket[::])
                return 
            for ind in range(val+1, n+1):

                bucket.append(ind)

                answer(ind)

                bucket.pop()
        answer(0)
        return ans