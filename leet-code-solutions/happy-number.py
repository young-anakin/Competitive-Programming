class Solution:
    def isHappy(self, n: int) -> bool:
        val = str(n)
        multiple = {'0':0, '1':1, '2':4, '3':9, '4':16, '5':25, '6': 36, '7':49, '8':64, '9': 81}
        visited = set()
        sum = 0
        new_val = ""
        flag = True
        while flag:
            for a in range(0, len(val)):
                sum += multiple[val[a]]
            # print(sum)
            if sum == 1:
                return True
            else:
                if val not in visited:
                    visited.add(val)
                    val = str(sum)
                else:
                    flag = False
                sum = 0
        return False