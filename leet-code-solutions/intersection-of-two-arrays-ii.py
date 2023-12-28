class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin = []
        for a in nums1:
            if a in nums2:
                fin.append(a)
                nums2.pop(nums2.index(a))
        return fin            
            