class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sSize = len(s)-1
        gSize = len(g)-1
        s.sort()
        g.sort()
        sinit = 0
        ginit = 0
        count = 0
        while sSize >= sinit and gSize >= ginit:
            if s[sSize] < g[gSize]:
                gSize -=1
            else:
                sSize -=1
                gSize -=1
                count +=1
        return count
