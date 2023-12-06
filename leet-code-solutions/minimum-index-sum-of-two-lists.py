class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = 1000000
        arr = []
        for i in range(0, len(list1)):
            if list1[i] in list2:
                low = i + list2.index(list1[i])
                # print(list1[i], " ", low)
                if low < minimum :
                    arr = []
                    minimum = low
                    arr.append(list1[i])
                elif low == minimum :
                    arr.append(list1[i])
        return arr