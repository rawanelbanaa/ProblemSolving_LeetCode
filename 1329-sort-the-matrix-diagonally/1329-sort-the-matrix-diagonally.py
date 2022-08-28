import numpy as np
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for x in range(m):
            mat[x] = mat[x][::-1]
        d = defaultdict(list)
        for x in range(m):
            for y in range(n):
                d[x+y].append(mat[x][y])
        for x in d:
            d[x].sort()
        for x in range(m):
            for y in range(n):
                mat[x][y] = d[x+y].pop(0)
        for x in range(m):
            mat[x] = mat[x][::-1]
        return mat