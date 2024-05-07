class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                result[i].append(1 if j == 0 or j == i  else result[i - 1][j - 1] + result[i - 1][j])
        return result
