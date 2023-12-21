from collections import defaultdict
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxxA = inf
        maxxB = inf
        for i in nums:
            if i > maxxA:
                return True
            if i<= maxxB:
                maxxB = i
            else:
                maxxA = i
        return False