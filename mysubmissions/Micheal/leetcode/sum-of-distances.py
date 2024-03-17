class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Approach : Put the numbers in an array and perform a prefix sum on them. After, for each index, calculate max - the index + index - min
        
        dd = defaultdict(list)

        for ind in range(len(nums)):
            dd[nums[ind]].append(ind)

        ps = defaultdict(list)
        for key, values in dd.items():
            sub = [0]
            for ind in range(len(values)):
                sub.append(values[ind] + sub[-1])
            sub.pop(0)
            ps[key] = sub
        
        ans = []

        checker = defaultdict(int)
        for ind, num in enumerate(nums):
            temp = 0
            temp2 = 0

            if checker[num] != 0:
                temp = checker[num] * dd[num][checker[num]]
                temp -= ps[num][checker[num]-1]
                print(temp)
            if checker[num] != len(ps[num])-1:
                sub = ps[num][-1] - ps[num][checker[num]]
                temp2 = sub - (dd[num][checker[num]] * ((len(ps[num]) -1) - checker[num]))

            ans.append(temp + temp2)
            checker[num] +=1

            # if checker[num] != len(ps[num]):
        return ans