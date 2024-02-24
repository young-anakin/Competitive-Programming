class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        print(arr)
        back = 0
        new = []
        print(arr)
        for ind in range(1,len(arr)+1):
            if arr[-ind] == "" or arr[-ind] == ".":
                continue
            elif arr[-ind] == "..":
                print(arr[ind])
                back +=1
                continue
            else:
                if back > 0:
                    back -=1
                    continue
                else:
                    new.append(arr[-ind])
            print(new)
        print(back)
        print(new)
        if len(new) == 0:
            return "/"
        new = [""] + new
        new = "/" + "/".join(new[::-1])
        # new = new[::-1]
        return new[0:len(new)-1]

