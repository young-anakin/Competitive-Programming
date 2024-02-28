class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Approach : Double the array and then use a monotonically decreasing stack to store the values of the next greater elements
        
        sub = []

        for ind in range(len(nums)):
            sub.append(nums[ind])

        sub.extend(nums)
        print(sub, nums)
        stack = []

        ans = [-1 for ind in range(len(nums))]
        n = len(nums)
        for ind in range(len(sub)):
            if len(stack) == 0:
                if ind <= n-1:
                    stack.append((sub[ind], ind))
            else:
                if stack[-1][0] > sub[ind]:
                    if ind <= n-1:
                        stack.append((sub[ind], ind))
                else:
                    while len(stack) != 0 and stack[-1][0] < sub[ind]:
                        x = stack.pop()
                        ans[x[1]] = sub[ind]
                    if ind <= n-1:
                        stack.append((sub[ind], ind))
        return ans

