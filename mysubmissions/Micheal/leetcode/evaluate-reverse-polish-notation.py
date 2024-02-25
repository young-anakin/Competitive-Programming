class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = []
        val = []
        # print(6//132)
        for ind in range(len(tokens)):
            if tokens[ind] == "+":
                a = val.pop()
                b = val.pop()
                val.append(a+b)
            elif tokens[ind] == "*":
                a = val.pop()
                b = val.pop()
                if a * b > 0:
                    val.append(math.floor(a*b))
                else:
                    val.append(math.ceil(a*b))
            elif tokens[ind] == "/":
                b = val.pop()
                a = val.pop()
                # x = a//b

                if a * b < 0:
                    val.append(math.ceil(a/b))
                else:
                    val.append(math.floor(a/b))
            elif tokens[ind] == "-":
                b = val.pop()
                a = val.pop()
                val.append(a-b)
            else:
                val.append(int(tokens[ind]))
            # print(val)
        return val[0]