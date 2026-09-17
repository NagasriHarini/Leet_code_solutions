class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        prefix = [0 for i in range(n)]
        prefix[0] = 1
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]

        suffix = [0 for i in range(n)]
        suffix[-1] = 1

        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        result = []

        for i in range(n):
            result.append(prefix[i]*suffix[i])

        return result

        