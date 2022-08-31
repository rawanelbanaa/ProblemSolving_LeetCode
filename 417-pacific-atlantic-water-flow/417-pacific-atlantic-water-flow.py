class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        setOne, setTwo = set(), set()
        
        def dfs(i, j, visited, prevHeight):
            if (i, j) in visited or heights[i][j] < prevHeight:
                return
            visited.add((i, j))
            
            if i != m - 1:
                dfs(i + 1, j, visited, heights[i][j])
            if i != 0:
                dfs(i - 1, j, visited, heights[i][j])
            if j != n - 1:
                dfs(i, j + 1, visited, heights[i][j])
            if j != 0:
                dfs(i, j - 1, visited, heights[i][j])
        
        for i in range(m):
            dfs(i, 0, setOne, 0)
            dfs(i, n - 1, setTwo, 0)
        
        for j in range(n):
            dfs(0, j, setOne, 0)
            dfs(m - 1, j, setTwo, 0)
        
        return list(map(list, setOne.intersection(setTwo)))