class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulo = (10**9 + 7)
        arr.sort()
        n = len(arr)
        newSet = set(arr)
        indexs = {num:i for i, num in enumerate(arr)}
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    num2 = arr[i]/arr[j]
                    if num2 in newSet:
                        index  = indexs[num2]
                        dp[i] += dp[j] * dp[index]
        
        return sum(dp) % modulo