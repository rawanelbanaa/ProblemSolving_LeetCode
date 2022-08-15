class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        temp = 0
        for x in range(len(s) - 1, -1, -1):
            ind = dic[s[x]]
            if temp > ind:
                result -= ind
                temp = ind
            else:
                temp = ind
                result += temp
        
        return result
    
    