import numpy as np
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = collections.defaultdict(list)

        for x, row in enumerate(mat):
            for y, num in enumerate(row):
                diagonals[x - y].append(num)
        
        for diagonal in diagonals.values():
            diagonal.sort(reverse=True)
        
        m, n = len(mat), len(mat[0])
        for x in range(m):
            for y in range(n):
                mat[x][y] = diagonals[x - y].pop()
        
        return mat