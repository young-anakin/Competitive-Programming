class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Approach : We use 2 pointer approach. we first define a dictionary to insert the prefix sum of each iteration in the list. We then check how many values we can chop off from each summ so that the difference between the prefix and goal has already been fulfiled. 
        
        #creating a dictionary
        cp = defaultdict(int)
        
        # make the cummulative at 0 increased by 1 because the goal subtracted from the current prefix can lead to 0 which is true but hasn't been introduced. 
        cp[0] += 1
        ans = 0 
        summ = 0
        for ind in range(len(nums)):
            summ += nums[ind]
            im = summ - goal
            ans += cp[im]
            cp[summ] +=1
        return ans


