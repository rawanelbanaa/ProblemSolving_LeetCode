class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in s:
            count = s.count(x)
            if count == 1:
                return s.index(x)
        return -1