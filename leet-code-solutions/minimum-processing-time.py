class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        tasks = list(reversed(tasks))
        processorTime.sort()
        minn = 0
        first = 0
        ans = []
        for a in range(len(processorTime)):
            time = processorTime[a]
            first = a * 4
            for b in range(4):
                minn = max(minn, time + tasks[b+first])
                print(time, tasks[b+first], " = ", time + tasks[b+first])
            ans.append(minn)
            minn = 0
        return max(ans)

