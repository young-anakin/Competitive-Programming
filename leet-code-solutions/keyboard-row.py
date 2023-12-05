class Solution(object):
    def findWords(self, words):
        arr1 = []
        arr2 = []
        arr3 = []
        for a in range(0, len("qwertyuiop")):
            arr1.append("qwertyuiop"[a])
        for b in range(0, len("asdfghjkl")):
            arr2.append("asdfghjkl"[b])
        for b in range(0, len("zxcvbnm")):
            arr3.append("zxcvbnm"[b])
        prev = 0
        res = []

        for word in words:
            old = word
            word = word.lower()
            if word[0] in arr1:
                prev = 1
            elif word[0] in arr2:
                prev = 2
            elif word[0] in arr3:
                prev = 3
            flag = True
            for b in range(0, len(word)):
                if word[b] in arr1:
                    if prev != 1:
                        flag = False
                        break
                elif word[b] in arr2:
                    if prev != 2:
                        flag = False
                        break
                elif word[b] in arr3:
                    if prev != 3:
                        flag = False
                        break
            if flag != False:
                res.append(old)
        return res
        