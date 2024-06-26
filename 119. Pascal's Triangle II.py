class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        triangle = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle[rowIndex]

#another solution
class Solution:
    def getRow(self, rowIndex: int, row = [1]) -> List[int]:
        return self.getRow(rowIndex - 1, [a + b for a, b in zip([0] + row, row + [0])]) if rowIndex else row