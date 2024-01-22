class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Approach : We change the even's to 0's and we change the odd's to 1's. we then calculate a prefix sum of the array. We keep a hash map for the prefixes as we go along and add the value of the prefixSum subtracted by k stored in the hashmap. (We initially set a value of 1 to 0 because subtracting a 0 from a subarray would create that specific answer).
        
        # defining hashmap
        checker = defaultdict(int)
        checker[0] = 1
        
        # updating the nums array to 1's and 0's by measure of eveness and oddness.
        for ind in range(len(nums)):
            if nums[ind]%2 == 0:
                nums[ind] = 0
            else:
                nums[ind] = 1
        
        # Calculate the prefix sum of the 1's and 0's
        prefix = [nums[0]]
        for ind in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[ind])
            
        ans = 0
        
        # append on answer the subarrays
        for ind in range(len(prefix)):
            ans += checker[prefix[ind]-k]
            checker[prefix[ind]] +=1
            
        return ans