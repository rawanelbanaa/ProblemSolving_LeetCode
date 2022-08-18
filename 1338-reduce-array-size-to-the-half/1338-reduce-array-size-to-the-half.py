class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        len_arr = len(arr)
        dic = {}
        res = 0
        for num in arr:
            dic[num] = dic.get(num, 0) + 1
        sorted_values = sorted(dic.values())
        while len_arr > len(arr)/2:
            len_arr -= sorted_values.pop()
            res +=1
        return res