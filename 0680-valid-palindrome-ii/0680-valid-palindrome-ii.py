class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                left_remove=s[i+1:j+1]
                right_remove=s[i:j]
                return left_remove==left_remove[-1::-1] or right_remove==right_remove[-1::-1]
            else:
                i+=1
                j-=1
        return True