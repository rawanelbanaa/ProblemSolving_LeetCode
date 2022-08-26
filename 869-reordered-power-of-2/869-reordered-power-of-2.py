class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        Total = set(itertools.permutations(str(n)))
        for x in Total:
            if x[0] == '0':
                continue
            num = int(''.join(x))
            if round(log(num, 2),9).is_integer():
                return True
        return False