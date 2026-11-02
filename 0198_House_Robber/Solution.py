class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        table = [0 for _ in range(n)]

        table[0] = nums[0]
        table[1] = max(nums[1],nums[0])

        for i in range(2,n):
            table[i] = max(table[i-1], table[i-2]+nums[i])

        return table[-1]

        