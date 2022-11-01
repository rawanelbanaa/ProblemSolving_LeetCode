class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for x,n in enumerate(nums):
            sub = target - n
            if sub in hashMap:
                return [hashMap[sub], x]
            hashMap[n] = x
        return