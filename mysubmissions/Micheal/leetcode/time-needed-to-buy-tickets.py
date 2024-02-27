class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        new = deque()

        for ind in range(len(tickets)):
            new.append(tickets[ind])
        cp = 0
        while new[k] != 1:
            for ind in range(len(tickets)):

                first = new[0]

                if first != 0:
                    cp +=1
                    first -=1
                new.popleft()
                new.append(first)
        for ind in range(k+1):
            if new[ind] != 0:
                cp +=1

            # print(new)
        return cp
                    
