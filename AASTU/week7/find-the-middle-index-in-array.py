class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Approach :  The question is to be solved by using prefix sum by iterating from left to right, for each index, we check wether it the one before it is equal to the largest value - the prefixSum at the index.
        
        # we initialize and create our prefixSum array that holds the sum of all the sarrays
        prefixSum = [0]
        for ind in range(len(nums)):
            prefixSum.append(prefixSum[-1] + nums[ind])
            
        last = prefixSum[-1]
        
        N = len(prefixSum)
            
        ans = -1
        for ind in range(1, N):
            if prefixSum[ind-1] == last - prefixSum[ind]:
                return ind-1
            
        return ans 
                
            
        