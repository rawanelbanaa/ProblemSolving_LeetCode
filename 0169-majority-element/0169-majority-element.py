class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_List = int(len(nums)/2)
        nums.sort()
        return nums[len_List]
            
