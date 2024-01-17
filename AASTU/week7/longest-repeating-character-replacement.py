class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cp = defaultdict(int)
        a = 0
        b = 0
        mx = 0
        ans = 0
        while b <= len(s)-1:
            cp[s[b]] +=1
            mx = max(cp.values())
            while ((b+1)-a) - mx > k:
                cp[s[a]] -=1
                if cp[s[a]] == 0:
                    del cp[s[a]]
                # mx = max(cp.values())
                a+=1
            ans = max((b+1)-a, ans)

            b +=1
        return ans

            