class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black = 0
        for ind in range(k):
            if blocks[ind] == "B":
                black +=1
        minn = k-black
        a = 0
        b = k
        while b <= len(blocks)-1:
            if blocks[a] == "B":
                black -=1
            a+=1
            if blocks[b] == "B":
                black +=1
            minn = min(minn, k-black)
            b +=1
        return minn