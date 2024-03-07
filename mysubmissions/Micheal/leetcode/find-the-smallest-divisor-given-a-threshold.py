class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        sm = 1000000000
        mx = 1111111111110
        while low <= high:
            md = (low + high)//2

            print(low, high, md)

            sm = sum([math.ceil(nums[i]/md) for i in range(len(nums))])
            print("Sum : ", sm)
            if sm > threshold:
                low = md + 1
            else:
                mx = min(md, mx)

                high = md -1

        return mx


