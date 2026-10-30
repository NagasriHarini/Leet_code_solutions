class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        curr_a = 0
        curr_b = 0
        out = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                curr_b = i
            else:
                if curr_a == curr_b:
                    out.append(str(nums[curr_a]))
                    curr_a = i
                    curr_b = i

                else:
                    temp = str(nums[curr_a])+"->"+str(nums[curr_b])
                    out.append(temp)
                    curr_a = i
                    curr_b = i

        if curr_a<len(nums):
            if curr_a == curr_b:
                out.append(str(nums[curr_a]))

            else:
                temp = str(nums[curr_a])+"->"+str(nums[curr_b])
                out.append(temp)          

        return out                
        