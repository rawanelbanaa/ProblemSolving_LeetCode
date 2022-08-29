class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited, numOflands = set(), 0

        def bfs(i, j):
            if i in range(rows) and j in range(cols) and (i, j) not in visited and grid[i][j] == "1":
                grid[i][j] = '0'
                visited.add((i, j))
                bfs(i + 1, j)  
                bfs(i - 1, j)  
                bfs(i, j + 1)  
                bfs(i, j - 1)  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    numOflands += 1

        return numOflands   