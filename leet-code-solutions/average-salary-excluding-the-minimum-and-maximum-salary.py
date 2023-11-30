class Solution(object):
    def average(self, salary):
        salary.sort()

        total = 0
        for a in range(1, len(salary) -1):
            print(salary[a])
            total += salary[a]
        return total/(len(salary)-2.0)
        