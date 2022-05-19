class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_words = s.split()
        return len(split_words[-1])