class Solution(object):
    def findAnagrams(self, s, p):
        dict1 = {}
        for a in range(0, len(p)):
            if p[a] not in dict1:
                dict1[p[a]] = 1
            else:
                dict1[p[a]]+=1
        dict2 = {}
        arr = []
        count = 0
        first = 0
        second = 0
        while(second != len(s)):
            if second - first == len(p):
                if dict1 == dict2:
                    arr.append(first)
                dict2[s[first]] -= 1
                if dict2[s[first]] == 0:
                    del dict2[s[first]]
                if s[second] not in dict2:
                    dict2[s[second]] = 1
                else:
                    dict2[s[second]] +=1
                first+=1
                second+=1
            else:
                if s[second] not in dict2:
                    dict2[s[second]] = 1
                else :
                    dict2[s[second]] +=1
                second +=1
            if second == len(s):
                if dict2 == dict1:
                    arr.append(first)
        return arr
        