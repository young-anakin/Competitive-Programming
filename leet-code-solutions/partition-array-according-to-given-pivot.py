class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        count = 0
        nums.append('a')
        a = 0
        while nums[a] != 'a':
            # print(nums[a], pivot)
            if nums[a] == pivot:
                # print(a)
                nums.pop(a)
                count +=1
            elif nums[a] < pivot:
                # print("hey")
                before.append(nums.pop(a))
                # continue
            else:
                a+=1
        for a in range(0, count):
            before.append(pivot)
        nums.pop(-1)
        return before + nums