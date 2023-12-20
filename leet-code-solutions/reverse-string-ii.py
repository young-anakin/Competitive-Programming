class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = 0
        n = len(s)
        new_str = ""
        last = True
        while a < n:
            if a+k<=n:
                v = s[a:a+k]
                a = a+k
                new_str += v[::-1]
                if a+k<=n:
                    v = s[a:a+k]
                    a = a+k
                    new_str += v[::]
                    last = not(last)
                else:
                    new_str += s[a:]
                    break
                last = not(last)
                print(last)
            else:
                v = s[a:]
                if last == True:
                    new_str += v[::-1]
                else:
                    new_str += v[::]
                # print(last)
                break
        return new_str