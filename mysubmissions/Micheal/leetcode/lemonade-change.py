class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dd = defaultdict(int)
        # for ind in range(len(bills)):
        for ind in range(len(bills)):
            dd[bills[ind]] +=1
            if bills[ind] == 5:
                continue
            if bills[ind] == 10:
                if dd[5] == 0:
                    return False
                dd[5] -=1
            if bills[ind] == 20:
                if (dd[10] <= 0):
                    if dd[5] < 3:
                        return False
                    dd[5] -=3
                else:
                    if dd[5] < 1:
                        return False
                    dd[10] -=1
                    dd[5] -=1
        return True
        print(dd)