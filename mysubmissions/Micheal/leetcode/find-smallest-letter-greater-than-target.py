class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        val =  bisect_right(letters, target)

        if val >= len(letters):
            return letters[0]
        return letters[val]