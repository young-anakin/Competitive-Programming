class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newStr = ""
        N = len(s)
        spaces.append(N+1)
        for i in range(0, N):
            if spaces[0] == i:
                newStr += " "
                newStr += s[i]
                spaces.pop(0)
            else:
                newStr += s[i]
        return newStr