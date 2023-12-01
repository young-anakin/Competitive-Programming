class Solution(object):
    def isAlienSorted(self, words, order):
        flag = False
        for a in range(0, len(words)-1):
            for b in range(0, min(len(words[a]), len(words[a+1]))):
                if order.index(words[a][b]) < order.index(words[a+1][b]):
                    flag = False
                    break
                    flag = False
                elif order.index(words[a][b]) == order.index(words[a+1][b]):
                    flag = True
                else:
                    return False
            if flag == True:
                if len(words[a]) > len(words[a+1]):
                    return False
        return True
        