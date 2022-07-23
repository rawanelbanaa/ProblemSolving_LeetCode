class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def binary_search(ls, value):
            left, right = 0, len(ls) - 1
            while left < right:
                mid = (left + right) // 2
                if ls[mid] >= value:
                    right = mid
                elif ls[mid] < value:
                    left = mid + 1
            return right
                
        sorted_nums = sorted(nums)
        counts = []
        for i in range(len(nums)):
            pos = binary_search(sorted_nums, nums[i])
            counts.append(pos)
            del sorted_nums[pos]
        return counts