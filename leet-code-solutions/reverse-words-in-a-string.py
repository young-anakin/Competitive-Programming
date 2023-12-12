class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arrWithoutSpace = []
        # print(arr)
        for a in range(1, len(arr)+1):
            if arr[-a] != "":
                arrWithoutSpace.append(arr[-a])
    
        return " ".join(arrWithoutSpace)