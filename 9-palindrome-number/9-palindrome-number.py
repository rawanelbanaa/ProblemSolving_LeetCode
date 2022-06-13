class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 : return False
        
        num = 1
        while x >= 10*num:
            num *= 10
            
        while x:
            if x // num != x%10:  return False
            x =(x% num) // 10
            num = num /100
        return True