class Solution(object):
    def printVertically(self, s):
        size = []
        arr = list(s.split(" "))
        for a in arr:
            size.append(len(a))
        maxs = max(size)

        output = []
        # print(size)
        # print(maxs)
        for a in range(0, maxs):
            strs = ""
            last = 0
            for b in arr:
                if len(b)-1 < a:
                    strs += " "
                    last +=1
                else:
                    strs += b[a]
                    last = 0
            output.append(strs[0:len(strs)-last])
        return output
        