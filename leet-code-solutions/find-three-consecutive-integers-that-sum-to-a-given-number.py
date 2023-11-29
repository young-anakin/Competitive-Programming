class Solution(object):
    def sumOfThree(self, num):
        val = num%3
        if val != 0:
            return []
        else:
            return [int(num/3)-1,int(num/3),int(num/3)+1]
        