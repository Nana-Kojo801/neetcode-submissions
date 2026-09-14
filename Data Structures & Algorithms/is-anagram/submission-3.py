class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds, dt = {}, {}

        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        
        for c in ds:
            if c not in dt or ds[c] != dt[c]:
                return False
        return True