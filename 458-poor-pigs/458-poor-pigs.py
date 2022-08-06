class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
           pgs = 0
            
           while(minutesToTest / minutesToDie +1 ) ** pgs < buckets:
                pgs += 1
           return pgs
        