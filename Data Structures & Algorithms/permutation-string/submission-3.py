class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for l in range(len(s2)):
            if sorted(s1) == sorted(s2[l:l+len(s1)]):
                return True
        return False