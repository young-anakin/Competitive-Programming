class Solution(object):
    def multiply(self, num1, num2):
        libr = {'0' : 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6 , '7': 7, '8': 8, '9': 9}
        num1 = num1[::-1]
        num2 = num2[::-1]
        print(num1, num2)
        prod = 0
        for a in range(0, len(num1)):
            val1 = num1[a]
            rem = 0
            mul = 0
            fin = ""
            for b in range(0, len(num2)):
                val2 = num2[b]
                mul = libr[val1] * libr[val2]
                print(val1, val2 , " = ", mul, rem)
                mul = mul + rem
                rem = str(mul)[0:-1]

                if rem == "":
                    rem = 0
                else:
                    rem = int(rem)
                fin += str(mul)[-1]
            fin += str(rem)
            fin = fin[::-1]
            if fin[0] == '0':
                fin = fin[1:]
            for c in range(0, a):
                fin += "0"
            prod += int(fin)


            print(fin)

        return str(prod)
        