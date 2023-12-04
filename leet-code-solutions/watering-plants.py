class Solution(object):
    def wateringPlants(self, plants, capacity):
        orig_cap = capacity
        steps = 0
        for a in range(0, len(plants)):
            if capacity - plants[a] >= 0:
                steps += 1
                capacity -= plants[a]
            else:
                capacity = orig_cap
                capacity -= plants[a]
                steps += 2*a +1

            print(capacity, " ", steps)
        return steps
        
        