class Solution(object):
    def romanToInt(self, s):
        precedence = {'I':0, 'V':1, 'X':2, 'L':3, 'C':4, 'D':5, 'M':6}
        exceptions = {'IV' : 4, 'IX': 9, 'XL' : 40, 'XC': 90, 'CD':400, 'CM': 900}
        values = {'I':1, "V":5, 'X':10, "L":50, "C":100, "D":500, 'M':1000 }
        a = 0
        b = 1
        sum = 0
        flag = ""
        while(b <= len(s)-1):
            if precedence[s[a]] < precedence[s[b]]:
                flag = "Add"
                sum += exceptions[s[a]+s[b]]
                a+=2
                b+=2
            else:
                flag = "No"
                sum += values[s[a]]
                a +=1
                b +=1
        print(sum)
        # if flag == "No":
        #     sum += values[s[len(s)-1]]
        if a > len(s)-1:
            pass
        else: 
            sum += values[s[len(s)-1]]
        
        
        return sum
                
            
        