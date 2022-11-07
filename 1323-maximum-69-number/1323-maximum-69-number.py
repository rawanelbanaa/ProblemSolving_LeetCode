class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))        
        
        
#         number = str(num)
#         length_num = len(number)
#         for x in range(0,length_num+1):
#             if number[x] != 9:
#                 number[x] == 9
#                 break
#             else:
#                 continue
                
#         return number