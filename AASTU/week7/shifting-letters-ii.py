class Solution:
    def shiftingLetters(self, s, shifts):
        # Approach (Prefix sum solution) : We create an array of zeroes and and in the begining of the changed index, we add a 1 if third index is 1 and -1 if third index is 0. We then add +1 (if third index is 0) and -1 (if third index is 1) so that the sum after the second index is unchanged.

        # mapping alphabets to integers from 0 to 25
        numbers = {}
        alphStr = "abcdefghijklmnopqrstuvwxyz"
        for i in range(0, len(alphStr)):
            numbers[alphStr[i]] = i+1


        #mapping integers to alphabets
        alphabets = {}
        alphStr = "abcdefghijklmnopqrstuvwxyz"
        for i in range(0, len(alphStr)):
            alphabets[i] = alphStr[i]

        answer = [] # array to store changes
        N = len(s) # length of the string

        # creating an array of 0's
        for ind in range(len(s)):
            answer.append(0)

        # Annotating the changes in the indexes that need to occur
        for shift in shifts:
            direction = shift[2]
            start = shift[0]
            end = shift[1]
            if direction == 1:
                answer[start] += 1
                if end + 1 < N:
                    answer[end + 1] += -1
            else:
                answer[start] -= 1
                if end + 1 < N:
                    answer[end + 1] += 1

        # creating an array for the prefix Sum
        prefixArray = [0]

        # Filling in the prefixSum for the entire array
        for ind in range(N):
            prefixArray.append(prefixArray[-1] + answer[ind])
        prefixArray.pop(0)


        finalStr = "" # string to return for changed alphabets

        # adding the new letter to finalStr
        for ind in range(len(s)):
            val = ((prefixArray[ind] + numbers[s[ind]])-1) % 26 # check where lies the new index of the letter after changes. ( modulo 26 applied for circular arrays,
            finalStr += alphabets[val]
        return (finalStr)