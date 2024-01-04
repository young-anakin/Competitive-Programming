class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l <= r:
            if s[r] == " ":
                r -=1
            elif s[l] == " ":
                l+=1
            elif not(97 <= ord(s[r].lower()) <= 122) and not(48 <= ord(s[r]) <= 57):
                r -=1
            elif not(97 <= ord(s[l].lower()) <= 122) and not(48 <= ord(s[l]) <= 57):
                l+=1
            else:
                if s[r].lower() != s[l].lower():
                    print(s[r], s[l])
                    return False
                r-=1
                l+=1
        return True

