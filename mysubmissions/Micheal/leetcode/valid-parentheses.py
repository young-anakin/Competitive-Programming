class Solution:
    def isValid(self, s: str) -> bool:
        dd = defaultdict(int)
        arr = []
        opened = []
        closed = []
        if len(s) == 1:
            return False
        for ind in range(1, len(s)+1):
            # print("ya")
            # print(s[-ind])
            if s[-ind] == ")" or s[-ind] == "}" or s[-ind] == "]":
                closed.append(s[-ind])
            else:
                if len(closed) == 0:
                    return False
                if s[-ind] == "[":
                    if closed[-1] != "]": 
                        return False
                    else:
                        closed.pop()
                elif s[-ind] == "(":
                    print(closed)
                    if closed[-1] != ")":
                        return False
                    else:
                        closed.pop()
                else:
                    if closed[-1] != "}":
                        return False
                    else:
                        closed.pop()
            # print(closed)
        if len(closed) != 0:
            return False
        return True
