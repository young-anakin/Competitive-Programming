class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(1, len(num)+1):
            # print(num[-1])
            if int(num[-i]) %2 != 0:
                # print(num[-i])
                return num[0:-i] + num[-i]
        return ""