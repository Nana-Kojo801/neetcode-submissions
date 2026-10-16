class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(m):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1

        matches = sum(
            count1[i] == count2[i] for i in range(26)
        )

        for r in range(m, n):
            if matches == 26:
                return True

            # Add character entering the window
            idx = ord(s2[r]) - 97
            count2[idx] += 1

            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] - 1 == count1[idx]:
                matches -= 1

            # Remove character leaving the window
            idx = ord(s2[r - m]) - 97
            count2[idx] -= 1

            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] + 1 == count1[idx]:
                matches -= 1

        return matches == 26