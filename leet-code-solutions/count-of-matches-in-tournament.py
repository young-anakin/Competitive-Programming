class Solution(object):
    def numberOfMatches(self, n):
        sum = 0
        while n > 1.0:
            if n%2 == 0:
                n = n/2
                sum += n
            elif n%2 == 1:
                n = n//2
                sum += n
                n += 1
            # print(n)
        return int(sum)
        