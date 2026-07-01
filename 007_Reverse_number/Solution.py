class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        duplicate = abs(x)
        res = 0 
        while duplicate>0:
            res = res*10+duplicate%10
            duplicate = duplicate//10

        if x<0:
            res = -res

        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res

        