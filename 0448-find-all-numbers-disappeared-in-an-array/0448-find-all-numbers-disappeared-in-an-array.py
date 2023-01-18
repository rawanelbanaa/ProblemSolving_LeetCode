class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if(len(nums) < 1):
            return []
        n = len(nums)
        return list(set(range(1,n+1)) - set(nums))
