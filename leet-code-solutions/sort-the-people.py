class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for a in range(len(heights)-1):
            for b in range(len(heights)-1-a):
                if heights[b] < heights[b+1]:
                    heights[b], heights[b+1] = heights[b+1], heights[b]
                    names[b], names[b+1] = names[b+1], names[b]
        return names