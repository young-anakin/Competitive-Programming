class Solution(object):
    def freqAlphabets(self, s):
        real = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}

        fake = {'10#': 'j', "11#": 'k', "12#": 'l', "13#": 'm', "14#": 'n', "15#": 'o', "16#": 'p', "17#": 'q', "18#": 'r',
                "19#": 's', "20#": 't', "21#": 'u', "22#": 'v', "23#": 'w', "24#": 'x', "25#": 'y', "26#": 'z'}
        fin = ""
        arr = []
        for a in range(0, len(s)):
            arr.append(s[a])
        for a in range(0, len(arr)):
            if arr[-1] == '#':
                val = ""
                a = arr.pop()
                b = arr.pop()
                c = arr.pop()
                val += c
                val += b
                val += a
                fin += fake[val]
            else:
                a = arr.pop()
                fin += real[a]
            if len(arr) == 0:
                break
        return fin[::-1]

        
        
            
            
            