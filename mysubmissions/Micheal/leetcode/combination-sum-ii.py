class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        # [4,4,2,1,4,2,2,1,3]


        final = []
        bucket = []
        self.x = None

        def backtrack(i):
            if sum(candidates) < target:
                return []
            if sum(bucket) == target:
                xz = bucket[::]
                xz.sort()
                if xz not in final:
                    final.append(xz[::])
                return 
            
            if sum(bucket) > target or len(candidates) <= i:
                return 
            if self.x != candidates[i]:
                bucket.append(candidates[i])
                backtrack(i+1)
                self.x = bucket.pop()
            backtrack(i+1)
        backtrack(0)
        return final
                
            
