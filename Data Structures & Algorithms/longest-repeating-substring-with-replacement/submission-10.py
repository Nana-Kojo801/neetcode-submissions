class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        maxFreq = 0

        l = 0

        for r in range(len(s)):
            idx = ord(s[r]) - 65
            count[idx] += 1
            maxFreq = max(maxFreq, count[idx])

            if (r - l + 1) - maxFreq > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
        return len(s) - l