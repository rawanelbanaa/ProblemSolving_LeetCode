class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        ext = q 
        ref = p
        
        while ext % 2==0 and ref % 2 == 0:
            ext /= 2
            ref /= 2
            
        if ext % 2 ==0 and ref % 2 !=0: return 0
        if ext % 2 ==1 and ref % 2 ==0: return 2
        if ext % 2 ==1 and ref % 2 !=0: return 1
        