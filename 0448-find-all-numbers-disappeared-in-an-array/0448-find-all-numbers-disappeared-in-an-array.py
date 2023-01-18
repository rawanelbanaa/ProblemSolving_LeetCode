class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if(len(nums) < 1):
            return []
        n = len(nums)
        return list(set(range(1,n+1)) - set(nums))
    
#     solution1
#         Res= []
#         n = len(nums)
#         for i in range(1,n+1):
#             if i in nums:
#                 continue
#             else:
#                 Res.append(i)
        
#         return Res

       
# solution2
# return set(range(1, len(nums)+1)).difference(set(nums))