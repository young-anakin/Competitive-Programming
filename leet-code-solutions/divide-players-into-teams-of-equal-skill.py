class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        a = 0
        b = len(skill)-1
        checker = skill[b] + skill[a]
        ans = 0
        if (b+1) % 2 != 0:
            return -1
        for ind in range(int((b+1)/2)):
            if skill[a] + skill[b] != checker:
                return -1
            ans += skill[a] * skill[b]
            print(skill[a], skill[b])
            b -=1
            a +=1
        return ans