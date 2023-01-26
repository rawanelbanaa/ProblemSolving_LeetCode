class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
        
        return ''.join(
            sorted( 
                [str(num) for num in nums], 
                key= functools.cmp_to_key(cmp), 
                reverse=True
            )
        ).lstrip('0') or '0' #remove leading zeroes, if empty return 0