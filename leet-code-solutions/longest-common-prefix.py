class Solution(object):
    def longestCommonPrefix(self,strs):
        lenOfStrs = []
        for i in strs:
            lenOfStrs.append(len(i))

        x = sorted(lenOfStrs)
        minimum = strs[lenOfStrs.index(x[0])]
        flag = True
        fin = ""
        for i in range(0, len(minimum)):
            # print(minimum[i])
            for str in strs:
                if minimum[i] != str[i]:
                    return fin
            fin += minimum[i]
        return fin
        