class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:


        elements = collections.Counter(arr)
        return max(elements, key = lambda x: elements[x])