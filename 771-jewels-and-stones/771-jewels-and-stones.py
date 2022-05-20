class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            if i in stones:
                numberOffounded = stones.count(i)
                count = count + numberOffounded
        return count