class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0 
        pointer2 = len(nums)-1
        i = 0
        
        while pointer1<=pointer2 and i<=pointer2:
            if nums[i]==0:
                nums[pointer1],nums[i]=nums[i],nums[pointer1]
                pointer1+=1
                i+=1
            elif nums[i]==2:
                nums[pointer2],nums[i] = nums[i],nums[pointer2]
                pointer2 -=1
            else:
                i+=1

        return nums
        