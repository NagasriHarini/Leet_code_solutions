class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        n = len(t)
        j = 0

        for i in range(n):
            if j < len(s) and s[j] == t[i]:
                j += 1

        if j == len(s):
            return True

        return False