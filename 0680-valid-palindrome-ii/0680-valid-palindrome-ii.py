class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                leftPointer=s[i+1:j+1]
                rightPointer=s[i:j]
                return leftPointer == leftPointer[-1::-1] or rightPointer == rightPointer[-1::-1]
            else:
                i+=1
                j-=1
        return True