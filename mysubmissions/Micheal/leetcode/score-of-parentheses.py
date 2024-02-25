class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ind in range(len(s)):
            if s[ind] == "(":
                stack.append("(")
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    ans = 0
                    while stack[-1] != "(":
                        x = stack.pop()
                        ans += x
                    stack.pop()
                    stack.append(2 * ans)
            # print(stack)
        ans = 0
        for ind in range(len(stack)):
            ans += stack[ind]
        return ans