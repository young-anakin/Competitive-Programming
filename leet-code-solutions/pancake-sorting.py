class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        final = sorted(arr)
        print(final)
        answer = []
        if arr == final:
            return []
        n = len(final)
        ran = n 
        z = 1
        for a in range(n):
            val = arr.index(final[-z])
            arr = list(reversed(arr[0:val+1])) + arr[val+1:]
            answer.append(val+1)
            arr = list(reversed(arr[0:ran])) + arr[ran:]
            answer.append(ran)
            ran -=1
            z+=1
            if arr == final:
                break
            print(val, arr)
        return answer



