class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = { n: 0 for n in range(min(nums), max(nums)+2) }
        subseq = { n: 0 for n in range(min(nums)-1, max(nums)+1) }
        
        for n in nums: 
            count[n] += 1
            
        for n in nums:
            if not count[n]: 
                continue
            count[n] -= 1
            if subseq[n - 1]:
                subseq[n - 1] -= 1
                subseq[n] += 1
            elif count[n + 1] and count[n + 2]:
                 count[n + 1] -= 1
                 count[n + 2] -= 1
                 subseq[n + 2] += 1
            else:
                return False
            
        return True