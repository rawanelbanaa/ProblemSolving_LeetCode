class Solution:
    def isValid(self, s: str) -> bool:
        newStack = []
        dic = {")": "(", "}": "{", "]":"["}
        
        for x in s:
            if x in dic:
                if newStack and newStack[-1] == dic[x]:
                    newStack.pop()
                else:
                    return False
            else:
                newStack.append(x)
                
        return True if not newStack else False