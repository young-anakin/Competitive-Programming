class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        # Approach : To find the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days, we can use binary search.
        # We can set the minimum weight capacity of the ship to the maximum weight of any single package, since the ship must be able to carry at least one package.
        # We can set the maximum weight capacity of the ship to the sum of all the package weights, since the ship must be able to carry all the packages in a single day.
        # We can then use binary search to find the weight capacity of the ship that will result in all the packages being shipped within days days.
        # In each iteration of the binary search, we calculate the mid-point between the minimum and maximum weight capacities of the ship. We then simulate the shipment of the packages with this mid-point weight capacity, keeping track of the number of days required to ship all the packages.
        # If the number of days required to ship all the packages is greater than days, then we know that the weight capacity of the ship must be increased, so we set the minimum weight capacity to mid + 1.
        # Otherwise, we know that the weight capacity of the ship is sufficient, so we set the maximum weight capacity to mid.
        # We continue the binary search until the minimum weight capacity equals the maximum weight capacity.
        # At this point, the minimum weight capacity of the ship is the least weight capacity that will result in all the packages being shipped within days days. We return this value as the result of the function.
       
       
        mx = sum(weights)
        mn = max(weights)


        def checker(mn, mx, days):

            while mn != mx:
                count = 0
                cp = 0
                md = (mn + mx)//2
                for ind in range(len(weights)):
                    cp += weights[ind]

                    if cp > md:
                        count +=1
                        cp = 0
                        cp += weights[ind]
                if cp > 0 and cp <= md:
                    count +=1

                if count <= days:
                    mx = md
                elif count > days:
                    mn = md + 1

            return mn
        
        x = checker(mn, mx, days)

        if x == None:
            return 0
        return x
                    

