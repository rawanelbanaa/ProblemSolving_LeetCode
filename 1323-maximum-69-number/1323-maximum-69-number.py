class Solution:
    def maximum69Number (self, num: int) -> int:
        # return int(str(num).replace('6', '9', 1))        

        
        num_list = list(str(num))
        for x in range(len(num_list)):
            if num_list[x] == '6':
                num_list[x] = '9'
                break
            else:
                continue
                
        return int("".join(num_list))