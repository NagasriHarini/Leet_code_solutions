class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs)==0:
            return ""

        if len(strs)==1:
            return strs[0]

        prefix = strs[0]

        for i in range(1,len(strs)):
            j = 0 

            while j<len(prefix) and j<len(strs[i]):
                if prefix[j] != strs[i][j]:
                    break

                j += 1

            prefix = prefix[0:j]

            if len(prefix) ==0:
                return ""

        return prefix
