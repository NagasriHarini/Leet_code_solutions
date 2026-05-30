def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n = len(nums)
    i = 0
    pointer = n-1
    
    while i<=pointer:
        if nums[i]==val:
            nums[i],nums[pointer] = nums[pointer],nums[i]
            pointer -=1
        else:
            i+=1

    return pointer+1

            

