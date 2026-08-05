class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0 
        ans = 0
        for num in nums:
            if num == 1:
                curr +=1
            else:
                curr = 0

            ans = max(curr,ans)

        return ans
