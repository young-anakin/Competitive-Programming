class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        setSet = set(nums)
        setList = list(setSet)
        setList.sort()
        # print(setSet)
        print(setList)
        count = 0
        pos = {}
        for a in range(len(setList)):
            pos[setList[a]] = a
        print(pos)
        for a in range(len(nums)):
            count += pos[nums[a]]
        return count