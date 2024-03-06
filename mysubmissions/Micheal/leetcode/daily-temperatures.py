class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dd = defaultdict(list)
        mstack = []
        ans = [0 for ind in range(len(temperatures))]
        for ind in range(len(temperatures)):
            dd[temperatures[ind]].append(ind)
            while len(mstack) != 0 and temperatures[ind] > mstack[-1]:
                loc = mstack.pop()
                sub = dd[loc][-1]
                ans[sub] =  ind - dd[loc].pop()  
                if len(dd[loc]) == 0:
                    del dd[loc]
            mstack.append(temperatures[ind])
        return ans 



