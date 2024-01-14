class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Storing values for the start and end indexes of first and second List
        s1 = []
        e1 = []
        s2 = []
        e2 = []
        for ind in range(len(firstList)):
            s1.append(firstList[ind][0])
            e1.append(firstList[ind][1])
        for ind in range(len(secondList)):
            s2.append(secondList[ind][0])
            e2.append(secondList[ind][1])


        #Approach : check if the first index of the firsrList is in between the two indices of the seocndList and choose the maximum of the firstIndices and the minimum of the second indices. Increment according to which index has the greater end point
            
            
        answer = [] # used to store the pairs of the answers
        
        beg = 0 # to store indice of firstList index
        end = 0 # to store indice of both indeces of secondList
        while beg <= len(firstList)-1 and end <= len(secondList)-1:
            if s1[beg] <= s2[end] <= e1[beg] or s2[end] <= s1[beg] <= e2[end]:
                answer.append([max(s1[beg], s2[end]), min(e1[beg], e2[end])])
            if e2[end] <= e1[beg]:
                end += 1
            else:
                beg +=1
        return answer

                
        