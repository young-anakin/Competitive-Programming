class Solution(object):
    def largestGoodInteger(self, num):
        val = []
        a = 0
        while a+3 <= len(num):
            if num[a:a+3].count(num[a]) == 3:
                val.append(num[a:a+3])
            a+=1
        if len(val) == 0:
            return ""
        val.sort()
        return val[-1]
        