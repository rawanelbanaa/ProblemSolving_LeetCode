class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newList = []
        
        n = len(matrix)
        if n > k:
            matrix = matrix[:k]
            
        for i in matrix:
             newList.extend(i)
        
        return sorted(newList)[k-1]        