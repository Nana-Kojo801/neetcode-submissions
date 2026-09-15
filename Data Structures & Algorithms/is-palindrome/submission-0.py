class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
        sl = s.lower()

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and sl[l] not in alpha:
                l += 1
            while l < r and sl[r] not in alpha:
                r -= 1
            
            if sl[l] != sl[r]:
                return False
            else:
                l += 1
                r -= 1
        return True