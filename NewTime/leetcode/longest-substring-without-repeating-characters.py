from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = defaultdict(lambda: 0)
        l = 0
        maxSum = 0
        for a in range(len(s)):
            dict[s[a]] +=1
            if dict[s[a]] > 1:
                while dict[s[a]] != 1:
                    dict[s[l]] -=1
                    l +=1
            maxSum = max(maxSum, a - l+1)
        return maxSum