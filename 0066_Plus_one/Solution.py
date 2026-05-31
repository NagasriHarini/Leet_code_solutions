class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        i = n-1

        while digits[i]==9 and i>0:
            i -=1
        if i==0 and digits[i]==9:
            digits[i] = 1 
            digits.append(0)

        else:
            digits[i] +=1
    
        for i in range(i+1,n):
            digits[i] = 0

        return digits

        