class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for a in range(0, len(strs[0])):
            for b in range(0, len(strs)-1):
                if ord(strs[b][a]) > ord(strs[b+1][a]):
                    count +=1
                    break
        return count