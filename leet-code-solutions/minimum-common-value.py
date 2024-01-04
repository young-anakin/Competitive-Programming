class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0
        nL = len(nums1)-1
        nR = len(nums2)-1
        val = 10000000000
        while l <= nL and r <= nR:
            if nums1[l] == nums2[r]:
                val = min(val, nums1[l])
                l+=1
                r+=1
            elif nums1[l] < nums2[r]:
                l+=1
            elif nums1[l] > nums2[r]:
                r+=1
        if val == 10000000000:
            return -1
        return val