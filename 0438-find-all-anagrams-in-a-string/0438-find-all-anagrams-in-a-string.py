class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        sCount = Counter()
        res = []
        
        for i in range(len(s)):
            sCount[s[i]] += 1
            if i >= len(p):
                sCount[s[i - len(p)]] -= 1
                if sCount[s[i - len(p)]] == 0:
                    del sCount[s[i - len(p)]]
            if sCount == pCount:# we need starting index
                res.append(i - len(p) + 1)
        return res