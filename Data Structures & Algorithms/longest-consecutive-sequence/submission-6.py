class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_num = set(nums)
        m = 0

        for n in nums:
            if n - 1 in s_num:
                continue
            
            l = 0
            while l + n in s_num:
                l += 1
            m = max(m, l)
        
        return m
