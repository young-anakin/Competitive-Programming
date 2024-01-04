class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        count = 0
        while l<=r:
            if people[r] > limit:
                print(1)
                r-=1
            elif r == l:
                if people[r] <= limit:
                    count +=1
                    r-=1
            elif people[r] == limit:
                count +=1
                print(2)
                r -=1                
            elif people[r] + people[l] <= limit:
                l+=1
                print(3)
                r-=1
                count +=1

            elif people[r] + people[l] > limit:
                print(4)
                count +=1
                r -=1 
        return count

