class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first = []
        last = []
        
        ans = []

        dd = {}
        for ind in range(len(intervals)):
            first.append(intervals[ind][0])
            dd[intervals[ind][0]] = ind
            last.append(intervals[ind][1])

        first.sort()


        for ind in range(len(last)):
            val = bisect_left(first, last[ind])
            if val >= len(last):
                ans.append(-1)
            else:
                ans.append(dd[first[val]])
        
        return ans


