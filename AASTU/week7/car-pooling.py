class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Approach : We construct a prefix sum of where all the people are going to be picked up and dropped of and if we have a place (index) where they exceed the number of capacity, we return False.
        
        # construct an array for the prefix sum with length of the last drop off
        n = 0
        for ind in range(len(trips)):
            n = max(n, trips[ind][2])
        arr = [0 for ind in range(n)]
        
        # construct a predefined version to calculate the prefix sum for the array
        for trip in trips:
            if trip[1] == 0:
                arr[trip[1]] += trip[0]
                if arr[trip[1]] > capacity:
                    return False
                arr[trip[2]-1] -= trip[0]  
                continue              
            arr[trip[1] -1 ] += trip[0]
            arr[trip[2]-1] -= trip[0]
        print(arr)
        
        # construct the prefix sum
        prefix = [0]
        for ind in range(n):
            prefix.append(prefix[-1] + arr[ind])
        prefix.pop(0)

        print(prefix)
        
        #check if the values of the stops and pickups exceed capacity. If so return False
        for ind in range(n):
            if prefix[ind] > capacity: 
                return False
        return True