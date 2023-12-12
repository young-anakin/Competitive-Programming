class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        validNumbers = set()
        wrongNumbers = []
        for ind in range(0, len(fronts)):
            if fronts[ind] == backs[ind]:
                wrongNumbers.append(fronts[ind])
        for ind in range(0, len(fronts)):
            if fronts[ind] not in wrongNumbers:
                validNumbers.add(fronts[ind])
            if backs[ind] not in wrongNumbers:
                validNumbers.add(backs[ind])
        if len(validNumbers) == 0:
            return 0
        validList = list(validNumbers)
        validList.sort()
        return validList[0]        