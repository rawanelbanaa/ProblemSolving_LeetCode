class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        while q % 2==0 and p % 2 == 0:
            q /= 2
            p /= 2
            
        if q % 2 ==0 and p % 2 !=0: return 0
        if q % 2 ==1 and p % 2 ==0: return 2
        if q % 2 ==1 and p % 2 !=0: return 1
        