class NumMatrix(object):

    def __init__(self, matrix):
        self.vert = []
        self.horiz = []
        for ind in range(len(matrix)):
            sub = []
            x = 0
            for y in range(len(matrix[0])):
                x += matrix[ind][y]
                sub.append(x)
            self.vert.append(sub)
        for ind in range(1, len(matrix)):
            for y in range(len(matrix[0])):
                self.vert[ind][y] += self.vert[ind-1][y]
        # print(self.vert)
    def sumRegion(self, row1, col1, row2, col2):
        ans = self.vert[row2][col2]
        if col1-1 >=0:
            ans -= self.vert[row2][col1-1]
        if row1-1 >= 0:
            ans -= self.vert[row1-1][col2]
        if row1-1>=0 and col1-1 >= 0:
            ans += self.vert[row1-1][col1-1]
        return ans

        return (self.vert[row2][col2] - self.vert[row2][col1-1]) - self.vert[row1-1][col2] + self.vert[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)