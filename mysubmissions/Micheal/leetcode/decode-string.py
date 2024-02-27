class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            ans = []
            n = len(s)
            i = 0
            # print(s)
            while i < n: 
                new = ""
                if s[i] in "0123456789":                
                    num = ""
                    while s[i] in "0123456789":
                        
                        num += s[i]
                        
                        i +=1
                    num = int(num)

                    op = 1
                    i+=1

                    while op != 0:
                        if s[i] == "[":
                            op +=1

                            new += "["
                        elif s[i] == "]":
                            op -=1
                            if op != 0:
                                new += "]"
                        else:
                            new += s[i]
                        i+=1
                    ans.append(decode(new) * num)

                else:
                    ans.append(s[i])
                    i+=1
            return "".join(ans)
        ans = decode(s)
        return ans
        
        
                
