class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefixSum = 0
        arr = []
        for x in nums:
            if x%2 == 0:
                prefixSum += x
        for x in queries:
            sum = nums[x[1]] + x[0]
            if sum % 2 == 0:
                if nums[x[1]] %2 != 0:
                    prefixSum += sum
                else:
                    prefixSum -= nums[x[1]]
                    prefixSum += sum


            else:
                if nums[x[1]]%2 == 0:
                    prefixSum -= nums[x[1]]
            nums[x[1]] = sum
            arr.append(prefixSum)

        return arr

        