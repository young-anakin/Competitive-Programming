class Solution(object):
    def sortSentence(self, sentence):
        dict = {}
        orig = 0
        sentence = sentence + " "
        for a in range(0, len(sentence)):
            if sentence[a] == " ":
                if type(int(sentence[a-1])) == type(2):
                    b = sentence[a-1]

                    dict[sentence[a-1]] = sentence[orig:sentence.index(str(sentence[a-1]))]
                    # orig = sentence.index()
                    orig = sentence.index(b)+2
        # print(dict)
        lows = sorted(dict)
        # print(lows)
        arr = []
        for a in lows:
            arr.append(dict.get(a))
        return " ".join(arr)