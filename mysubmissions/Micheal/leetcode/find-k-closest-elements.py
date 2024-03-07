class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []

        val = bisect_left(arr, x)


        cp = 0

        l = val
        n = len(arr)
        r = val
        if val < n:
            if arr[val] == x:
                ans.append(arr[val])
                l -=1
                r +=1
                cp = 1
            else:
                l = val - 1
                r = val
        else:
            l = val - 1
            r = val
        while len(ans) < k:
            if l >= 0 and r < n:
                if abs(arr[l] - x) < abs(arr[r] - x):
                    ans.append(arr[l])
                    l -=1
                elif abs(arr[l] - x) == abs(arr[r] - x):
                    if arr[l] > arr[r]:
                        ans.append(arr[r])
                        r +=1
                    else:
                        ans.append(arr[l])
                        l-=1
                else:
                    ans.append(arr[r])
                    r +=1
            elif l < 0:
                ans.append(arr[r])
                r+=1
            else:
                ans.append(arr[l])
                l -=1
        ans.sort()
        return ans

