class Solution(object):
    def mergeAlternately(self, word1, word2):
        a = 0
        b = 0
        length = min(len(word1), len(word2))
        fin = ""
        while a < length and b < length:
            fin += word1[a]
            fin += word2[b]
            a+=1
            b+=1
        if len(word1) < len(word2):
            fin += word2[b:]
        elif len(word2) < len(word1):
            fin += word1[a:]
        return fin
            
        