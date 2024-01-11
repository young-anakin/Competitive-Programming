class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cp = 0
        vowel = "aeiou"
        maxx = 0
        a = 0
        b = k
        for i in range(k):
            if s[i] in vowel:
                cp +=1
        maxx = cp
        while b <= len(s)-1:
            if s[a] in vowel:
                cp -=1
            if s[b] in vowel:
                cp +=1
            maxx = max(maxx, cp)
            a+=1
            b+=1
        return maxx