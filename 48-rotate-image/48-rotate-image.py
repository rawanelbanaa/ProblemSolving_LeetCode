import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=np.array(matrix)
        b=np.rot90(a,3)
        x=[]
        for i in b:
            x.append(i)
            matrix.clear()
            matrix.extend(x)