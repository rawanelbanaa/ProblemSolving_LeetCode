class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: 
            return 1
        
        prev = [i for i in range(n, 1, -1)]
        for x in range(m-2):
            
            curnt = [0]*(n-1)
            for i in range(n-1, 0, -1):
                if i == n-1:
                    curnt[i-1] = 1 + prev[i-1]
                    continue

                curnt[i-1] = prev[i-1] + curnt[i]
            
            prev = curnt
            
        return prev[0]