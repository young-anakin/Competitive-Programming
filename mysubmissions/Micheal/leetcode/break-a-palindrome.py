class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        if len(palindrome) == palindrome.count('a'):
            return palindrome[0:len(palindrome)-1] + 'b'
        
        for ind in range(len(palindrome)):
            if palindrome[ind] != 'a':
                if len(palindrome) %2 == 1 and ind == len(palindrome)//2:

                    return palindrome[0:len(palindrome)-1] + chr(ord(palindrome[-1])+1)
                else:
                    return palindrome[0:ind] + 'a' + palindrome[ind+1:]
