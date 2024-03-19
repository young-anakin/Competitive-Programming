class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Approach : We keep checking (for every substring we split) if a smaller or upper form of it is in the substring. if it is, we hold on to the string. We keep checking for left and right of each letter where it's not included in upper and lower case.
        ans = ""
        for i in range(len(s)):
            if s[i].upper() in s and s[i].lower() in s:
                continue

            l = self.longestNiceSubstring(s[0:i])
            r = self.longestNiceSubstring(s[i+1:])
            return max(l, r, key = len)

        return s



