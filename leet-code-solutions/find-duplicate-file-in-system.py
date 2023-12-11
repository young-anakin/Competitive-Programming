class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        output = []
        files = {}
        for path in paths:
            values = path.split(' ')
            for val in range(1, len(values)):
                orig = values[val].index('(')
                ending = values[val].index(')')

                if values[val][orig + 1:ending] not in files:
                    files[values[val][orig + 1:ending]] = [values[0] + "/" + values[val][0:orig]]
                else:
                    # print("kaka")
                    files[values[val][orig + 1:ending]].append(values[0] + "/" + values[val][0:orig])
                # print(files)
        for values in files.values():
            if len(values) == 1:
                continue
            output.append(values)
        return output