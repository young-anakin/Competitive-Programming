class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cp = 0
        if maxDoubles == 0:
            return target - 1
        while True :
            # apply check (if target <= 1)
            if maxDoubles == 0:
                return (target - 1) + cp
            if target <= 1:
                return cp
            if target %2 == 0:
                maxDoubles -=1
                cp +=1
                target = target //2
            else:
                cp +=1
                target -=1
