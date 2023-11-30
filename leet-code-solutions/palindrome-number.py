class Solution(object):
    def isPalindrome(self, x):
        import math

        wow = str(x)

        if x % 2 == 0:
            les = int(len(wow) / 2)
        else:
            les = math.floor(int(len(wow) / 2))
        les = int(les)
        for a in range(0, les):
            if wow[a] != wow[-a - 1]:
                return False
        return True
