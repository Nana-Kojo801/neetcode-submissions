class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = maxF = 0

        for r in range(len(s)):
            idx = ord(s[r]) - 65
            count[idx] += 1
            maxF = max(maxF, count[idx])

            if r - l + 1 - maxF > k:
                count[ord(s[l]) - 65] -= 1
                l += 1

        return len(s) - l