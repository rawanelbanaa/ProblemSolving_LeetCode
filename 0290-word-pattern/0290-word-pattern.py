class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        dic ={}
        for i in range(len(pattern)):
            try:
                if ((pattern[i] in dic) or (words[i] in dic.values())) and (dic[pattern[i]] !=words[i]):
                    return False
            except KeyError:
                return False
            if words[i] not in dic.values():
                dic[pattern[i]] = words[i]
        return True
        
