class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        countOfRows = range(numRows - 1)
        
        for i in countOfRows:
            temp = [0] + result[-1] + [0]
            row = []
            for x in range(len(result[-1]) + 1):
                row.append(temp[x] + temp[x+1])
            result.append(row)
        return result