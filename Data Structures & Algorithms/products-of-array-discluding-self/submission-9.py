class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)

        p = 1
        for i in range(len(nums)):
            results[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= p
            p *= nums[i]
        return results