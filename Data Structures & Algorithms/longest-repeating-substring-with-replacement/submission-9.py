class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        res = l = 0
        most_freq = 0

        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            most_freq = max(most_freq, count[ord(s[r]) - 65])

            if (r - l + 1) - most_freq <= k:
                res = max(res, r - l + 1)
            else:
                count[ord(s[l]) - 65] -= 1
                l += 1
        return res
