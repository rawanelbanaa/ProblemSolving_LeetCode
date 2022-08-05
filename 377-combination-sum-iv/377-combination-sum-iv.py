class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
#         count =  0
#         for n in nums:
#             sub = target - n
#             if sub in nums :
                
        dic = {0 : 1}
        for total in range(1, target+1):
            dic[total] = 0
            for n in nums:
                dic[total] += dic.get(total-n, 0)
                
        return dic[target]
                