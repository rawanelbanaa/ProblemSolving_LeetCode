class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        dic, ls, lt = {}, len(stamp), len(target)
        def dfs(s, t, sequns):
            if t == lt:
                dic[s, t] = sequns if s == ls else []
            if (s, t) not in dic:
                if s == ls:
                    for i in range(ls):
                        cd = dfs(i, t, [t-i]+sequns)
                        if cd:
                            dic[s, t] = cd
                            break
                    else: 
                        dic[s, t] = []
                elif target[t] == stamp[s]:
                    cd = dfs(s+1, t+1, sequns)
                    dic[s, t] = cd if cd else dfs(0, t+1, sequns+[t+1])
                else:
                    dic[s, t] = []
            return dic[s, t]
        return dfs(0, 0, [0])