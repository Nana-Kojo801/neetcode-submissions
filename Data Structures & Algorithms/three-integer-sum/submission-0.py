class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        target = 0

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1

            # [-4, -1, -1, 0, 1, 2]

            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == target:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif summ < target:
                    j += 1
                else:
                    k -= 1
        return output



