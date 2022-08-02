class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newList = []
        
        for i in matrix:
             newList.extend(i)
        
        return sorted(newList)[k-1]        