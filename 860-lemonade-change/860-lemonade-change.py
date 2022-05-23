class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twen = 0
        for num in bills:
            if num != 5:
                if num == 10:
                    if five > 0:
                        five -= 1
                        ten += 1
                    else: return False

                if num == 20:
                    if ten > 0 and five > 0:
                        five -= 1
                        ten -= 1
                        twen += 1
                    elif five >= 3:
                        five -=3
                    else: return False
            else:
                five += 1

        return True  
            