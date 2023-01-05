this is my first solution in my mind but there are a runtime error



<code>
    class Solution:
        def lengthOfLastWord(self, s: str) -> int:
            res = 0
            for n in range(len(s)-1, -1, -1):
                if s[n] == " ":
                    if res == 0:
                        continue
                    else:
                        return res
                else:
                    res += 1>         
               
</code>
