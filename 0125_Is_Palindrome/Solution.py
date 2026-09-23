class Solution(object):
    def isPalindrome(self, s):
        i = 0
        n = len(s) - 1

        while i < n:

            while i < n and not s[i].isalnum():
                i += 1

            while i < n and not s[n].isalnum():
                n -= 1

            if s[i].lower() != s[n].lower():
                return False

            i += 1
            n -= 1
        

        return True