class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for num in bills:
            if num != 5:
                if num == 10:
                    if five > 0:
                        five -= 1; ten += 1
                    else: return False
                elif ten > 0 and five > 0:
                    five -= 1;ten -= 1
                elif five >= 3:
                    five -=3
                else: return False
            else:
                five += 1

        return True  
            