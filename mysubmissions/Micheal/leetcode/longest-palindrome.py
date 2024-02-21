class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict = defaultdict(int)
        for ind in range(len(s)):
            my_dict[s[ind]] += 1

        cp = 0
        odd = 0
        fl = True
        for key, values in my_dict.items():
            if values%2 == 0:
                cp += values
            else:
                fl = False
                cp += values - 1
        if fl == False:
            cp +=1
        return odd + cp