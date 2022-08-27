class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = float("-inf")
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            ltSum = [0] * m
            for x in range(i, n):
                curSum = 0
                curltSum = [0]
                for t in range(m):
                    ltSum[t] += matrix[t][x]
                    curSum += ltSum[t]
                    ind = bisect_left(curltSum, curSum - k)
                    if ind < len(curltSum):
                        if curltSum[ind] == curSum - k:
                            return k
                        else:
                            res = max(res, curSum - curltSum[ind])
                    insort(curltSum, curSum)
        return res