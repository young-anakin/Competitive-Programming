class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for ind in range(len(nums)):
            prefix.append(prefix[-1] + nums[ind])
        prefix.pop(0)
        ans = []
        # ans = 0
        n = len(nums)
        maxx = prefix[-1]
        print(prefix)
        print(maxx)
        for ind in range(len(prefix)):
            right = 0
            if ind != n-1:
                right = abs((maxx - prefix[ind]) - ((n-(ind+1)) * nums[ind]))
            left = 0
            if ind != 0:
                left = abs(prefix[ind-1] - (ind*nums[ind]))
            print(right, left)
            ans.append(right + left)
        return ans