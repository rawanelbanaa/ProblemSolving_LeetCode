class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        return sorted(nums)[-3] if len(nums) >= 3 else max(nums) 
            
                