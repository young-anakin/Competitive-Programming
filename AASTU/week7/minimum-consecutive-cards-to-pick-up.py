class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        a = 0
        b = 0
        summ = 0
        minn = 900000000
        cp = defaultdict(int)
        while b <= len(cards)-1:
            cp[cards[b]] +=1
            while cp[cards[b]] > 1:
                minn = min((b+1)-a, minn)
                cp[cards[a]] -=1
                a+=1
            b +=1
        if minn == 900000000:
            return -1
        return minn