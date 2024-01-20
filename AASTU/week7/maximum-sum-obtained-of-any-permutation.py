class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # Approach : We run a prefix sum for the requests. We calculate which index has the most frequency that is calculated so that we can make the largest value to that index and we decrement accordingly.(for all frequencies)
        
        # we sort because we want to make mapping easier
        nums.sort()
        
        # we calculate the prefix of the requests to calculate the frequency in which each index is added. 
        prefix = [0 for ind in range(len(nums))]
        for val in requests:
            prefix[val[0]] +=1
            if val[1] +1 != len(nums):
                prefix[val[1] +1 ] -=1
        ans = [0]
        for ind in range(len(nums)):
            ans.append(ans[-1] + prefix[ind])
        ans.pop(0)
        
        #We sort the answer we obtained to help with matching
        comparator = []
        comparator = sorted(ans)

        # We map the sorted nums list to the sorted power(frequency) that each index needs. So index with lowest frequency will be mapped with lowest value in our initial nums. 
        numPower = defaultdict(list)
        for ind in range(len(nums)):
            numPower[comparator[ind]].append(nums[ind])

        # we formulate an array to hold the values of nums in the frequencies that they appear.
        finalAns = []
        res = 0
        for ind in range(len(nums)):
            finalAns.append(numPower[ans[ind]].pop())
        # we calculate the final answer by multiplying the new positioned numbers by how many times that they are calculated.
        for ind in range(len(nums)):
            res += finalAns[ind] * ans[ind]
        return res % (pow(10,9) + 7)