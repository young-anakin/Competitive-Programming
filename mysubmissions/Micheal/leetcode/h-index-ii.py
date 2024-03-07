class Solution:
    def hIndex(self, citations: List[int]) -> int:
        mn = 0


        # if len(citations) == 1:
        #     return min(citations[0], 1)
        mx = len(citations)-1
        n = len(citations)
        while mn < mx:
            md = (mn + mx)//2


            if n - md <= citations[md] :
                mx = md
            else:
                mn = md + 1
            # print(mn, md, mx)
        ans = min(n - mx, citations[mx])
        return ans