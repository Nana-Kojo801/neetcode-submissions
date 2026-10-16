class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count s1 and the first window of s2
        for i in range(m):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1

        if count1 == count2:
            return True

        # Slide the window across s2
        for r in range(m, n):
            count2[ord(s2[r]) - 97] += 1  # Add new character
            count2[ord(s2[r - m]) - 97] -= 1  # Remove old character

            if count1 == count2:
                return True

        return False