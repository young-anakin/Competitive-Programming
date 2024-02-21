class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cp = 0

        # mx = 0
        mx = 0
        nums.append(n)
        a = 0
        while mx < n:
            if mx < nums[a]-1:
                mx += mx+1
                cp +=1
            else:
                mx += nums[a]
                a +=1
        return cp