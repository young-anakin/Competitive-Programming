class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        new = deque()
        deck.sort()
        deck = deck[::-1]
        print(deck)
        new.append(deck[0])
        for ind in range(1, len(deck)):
            val = new.pop()

            new.appendleft(val)

            new.appendleft(deck[ind])
        return new
