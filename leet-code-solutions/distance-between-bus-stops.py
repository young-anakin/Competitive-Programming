class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        maxx=max(start,destination)
        minn=min(start,destination)
        sum1=sum(distance[minn:maxx])
        sum2=sum(distance[:minn])+sum(distance[maxx:])
        return min(sum1,sum2)

        
        
        
        
        
        
        
        
        
        
        
#         prefix = [0]
#         for a in range(0, len(distance)):
#             prefix.append(distance[a] + prefix[-1])
#         a = prefix[destination] - prefix[start]
#         b = prefix[-1] - (prefix[destination] - prefix[start])

#         return min(a