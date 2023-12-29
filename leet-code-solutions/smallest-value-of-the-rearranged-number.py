class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = False
        if str(num)[0] == "-":
            negative = True
        arr = []
        val = str(num)
        zero = 0
        if len(val) == val.count('0'):
            return 0
        for a in range(len(val)):
            if val[a] == '0':
                zero +=1
                continue
            if negative:
                if a == 0:
                    continue
                else:
                    arr.append(val[a])
            else:
                arr.append(val[a])
        fin = ""
        arr.sort()
        print(arr)
        if negative:
            fin += "-"
            count = 1
            for a in range(0,len(arr)):
                fin += arr[-count]
                count +=1
            for b in range(zero):
                fin += '0'
        else:
            fin += arr[0]
            for a in range(zero):
                fin += '0'
            for a in range(1, len(arr)):
                fin += arr[a]
        
        return int(fin)
