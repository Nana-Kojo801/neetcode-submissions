class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        
        for l in range(len(s2)):
            # print(l, l+len(s1)-1)
            print(s2[l:l+len(s1)])
            if sorted(s1) == sorted(s2[l:l+len(s1)]):
                return True
        return False