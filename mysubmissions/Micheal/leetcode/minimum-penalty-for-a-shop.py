class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Approach : We do a prefix sum on the array twice, one where 'Y' = 1 and 'N' = 0 and one where it's the opposite.

        front = [0]
        back = [0]

        for ind in range(len(customers)):
            if customers[ind] == 'N':
                front.append(front[-1] + 0)
                back.append(back[-1] + 1)
            else:
                front.append(front[-1] + 1)
                back.append(back[-1] + 0)
        mx = max(front)
        check = 1000000000
        ans = 0
        for ind in range(len(front)):
            if check > (mx - front[ind]) + back[ind]:
                check = (mx - front[ind]) + back[ind]
                ans = ind
        # if ans == len(customers)-1 and len(customers) != ans:
        #     ans +=1
        return ans