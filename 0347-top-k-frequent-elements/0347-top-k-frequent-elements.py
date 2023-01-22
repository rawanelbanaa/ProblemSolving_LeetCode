class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int) 
        
        for num in nums:
            dic[num] += 1
        

        dic = dict(sorted(dic.items(), key = lambda item:item[1], reverse = True))
        result = [] 
        
        for key, value in dic.items():
            if k > 0:
                result.append(key)
                k -=1

        return result