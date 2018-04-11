class NumMatrix(object):

    def __init__(self, matrix):
        lenM = len(matrix)
        if lenM == 0:
            return 
        lenN = len(matrix[0])
        if lenN == 0:
            return
        
        self.f = [[0 for x in xrange(lenN+1)] for y in xrange(lenM+1)]
        for i in xrange(1, lenM+1):
            for j in xrange(1, lenN+1):
                self.f[i][j] = self.f[i-1][j] + self.f[i][j-1] - self.f[i-1][j-1] + matrix[i-1][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        if row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0 or row1 > row2 or col1 > col2:
            return 0
        
        return self.f[row2+1][col2+1] - self.f[row1][col2+1] - self.f[row2+1][col1] + self.f[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)