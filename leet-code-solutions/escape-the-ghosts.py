class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mins = 100000
        target_distance = abs(target[0]) + abs(target[1])
        print(abs(target_distance))
        for ghost in ghosts:
            val = abs(target[0] -  ghost[0]) + abs(target[1] - ghost[1])
            if val <= target_distance:
                return False
            if val < mins:
                mins = val
        return True