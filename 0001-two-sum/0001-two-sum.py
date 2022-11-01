class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
           
        for index , value in  enumerate(nums):
            num_needed = target - value
            if num_needed in hashMap:
                return [hashMap[num_needed], index]
            hashMap [value] = index
        return