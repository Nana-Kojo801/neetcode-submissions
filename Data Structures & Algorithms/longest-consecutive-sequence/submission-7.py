class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snum = set(nums)
        m = 0

        for n in snum:
            if n - 1 in snum:
                continue
            l = 0
            while n + l in snum:
                l += 1
            m = max(m, l)
        return m