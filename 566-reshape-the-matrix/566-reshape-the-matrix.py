import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        array_a = np.array(mat)
        sizeOfArray = array_a.size
        if sizeOfArray != r*c: return mat
        array_b = array_a.reshape(r,c)
        
        return array_b