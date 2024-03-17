class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()

        for ind in range(len(senate)):
            if senate[ind] == "R":
                R.append(ind)
            else:
                D.append(ind)
        while len(R) != 0 and len(D) != 0:
            if R[0] < D[0]:
                D.popleft()
                R.append(R.popleft()+len(senate))
            elif R[0] > D[0]:
                R.popleft()
                D.append(D.popleft()+len(senate))
        
        if len(R) != 0:
            return "Radiant"
        else:
            return "Dire"