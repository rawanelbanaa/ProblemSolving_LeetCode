class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        if len(strs)==1:
            
            return [strs]
        
        else:
            
            for i in range(len(strs)):
                value = ''.join(sorted(strs[i]))
                if value in dict:
                    dict[value].append(strs[i])
                else:
                    dict[value] = [strs[i]]
            return list(dict.values())