class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        helper_dic = {'I':1 , "V":5, "X":10 , "L":50, "C":100, "D":500, "M":1000}
        
        curr = s[len(s)-1]
        prev = curr
        res = helper_dic[curr]

        for i in range(len(s)-2,-1,-1):
            curr = s[i]
            if helper_dic[prev]>helper_dic[curr]:
                res -= helper_dic[curr]

            else:
                res += helper_dic[curr]

            prev = curr

        return res