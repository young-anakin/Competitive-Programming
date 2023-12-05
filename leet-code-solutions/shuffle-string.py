class Solution(object):
    def restoreString(self, s, indices):
        returnArr = []
        for a in range(0, len(s)):
            returnArr.append('0')
        for character in range(0, len(s)):
            returnArr[indices[character]] = s[character]
        returnString = ""
        for a in range(0, len(returnArr)):
            returnString += returnArr[a]
        return returnString