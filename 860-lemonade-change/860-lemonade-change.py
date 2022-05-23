class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for num in bills:
            if num != 5:
                if num == 10:
                    five -= 1; ten += 1
                elif ten > 0:
                    five -= 1;ten -= 1
                else:
                    five -=3
                if five < 0: return False
            else:
                five += 1

        return True  
            