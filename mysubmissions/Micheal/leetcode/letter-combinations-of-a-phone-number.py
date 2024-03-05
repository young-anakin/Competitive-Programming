class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        NumLetter = {"2" : "abc", "3" : "def", "4":"ghi", "5" : "jkl", "6": "mno", "7": "pqrs", "8" : "tuv", "9": "wxyz"}

        tot = []
        bucket = []
        
        if digits == "":
            return []
        def dial(digits, i):
            
            if len(digits) == len(bucket):
                tot.append("".join(bucket))
                return
            
            # if len(NumLetter[i]) > 

            for ind in range(i, len(digits)):
                s = digits[ind]
                
                for j in range(len(NumLetter[s])):
                    bucket.append(NumLetter[s][j])
                    dial(digits, i+1)
                    bucket.pop()
                break
        
        
        dial(digits, 0)
        return tot




