n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()
q = int(input())
# 3 6 8 10 11
for ind in range(q):
    val = int(input())
    low = 0
    high = n -1
    tot = 0
    while low <= high:
        md = (low+high)//2
        if arr[md] <= val:
            tot = max(tot, md+1)
            low = md + 1
        else:
            high = md -1
    print(tot)