class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for a in image:
            a = a.reverse()
        # print(image)
        for a in range(len(image)):
            for b in range(len(image)):
                if image[a][b] == 0:
                    image[a][b] = 1
                else:
                    image[a][b] = 0
        return image