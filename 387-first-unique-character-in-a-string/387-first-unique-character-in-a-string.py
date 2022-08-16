class Solution:
    def firstUniqChar(self, s: str) -> int:
        sea = Counter(s)
        for key, val in sea.items():
            if val==1:
                return s.index(key)
        return -1