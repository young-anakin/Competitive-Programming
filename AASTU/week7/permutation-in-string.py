class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        ds = defaultdict(lambda : 0)
        for ind in range(len(s1)):
            ds[s1[ind]] +=1
        checked = defaultdict(lambda : 0)
        for ind in range(len(s1)):
            checked[s2[ind]] +=1
        a, b = 0,len(s1)
        print(ds)
        if checked == ds:
            return True
        while b<= len(s2)-1:
            print(checked)

            checked[s2[a]] -=1
            checked[s2[b]] +=1
            if checked[s2[a]] == 0:
                del checked[s2[a]]
            if checked == ds:
                return True
            a +=1
            b +=1
            
        return False
