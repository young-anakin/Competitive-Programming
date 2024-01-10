class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = 0
        b = 0
        while b < len(typed):
            if a < len(name) and name[a] == typed[b]:
                a +=1
                b +=1
            elif b == 0 or typed[b] != typed[b-1]:
                return False
            else:
                b+=1
            
        return a == len(name)
            