class Solution(object):
    def subdomainVisits(self, cpdomains):
        dict = {}
        strs = ""

        for a in range(0, len(cpdomains)):
            val = cpdomains[a].find(" ")
            strs = cpdomains[a][val+1:]
            if strs not in dict:
                dict[strs] = int(cpdomains[a][0:val])
            else:
                dict[strs] += int(cpdomains[a][0:val])
            for b in range(0, len(strs)):
                if strs[b] == ".":
                    if strs[b+1:] not in dict:
                        dict[strs[b+1:]] = int(cpdomains[a][0:val])
                    else:
                        dict[strs[b+1:]] += int(cpdomains[a][0:val])
        fin_arr = []
        for key, values in dict.items():
            fin_arr.append(str(values) +  " " + key)
        return fin_arr
