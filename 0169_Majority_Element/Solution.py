class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        n = len(nums)
        val = nums[0]
        for i in range(1,n):
            if counter == 0:
                val = nums[i]

            if nums[i] == val:
                counter += 1
        
            else:
                counter -= 1

        return val 

            

                




        