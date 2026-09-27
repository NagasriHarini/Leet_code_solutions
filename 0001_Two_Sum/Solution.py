class Solution:
    def twoSum(self, nums, target: int):

        # here seen is a dictionary that will store the numbers we have seen so far and their corresponding indices
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i