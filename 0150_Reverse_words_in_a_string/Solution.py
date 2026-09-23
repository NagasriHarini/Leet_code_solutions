class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        n = len(s)
        current_word = ""
        result = ""
        i = n-1
        
        while i>=0:
            if s[i] == " ":
                result = result + current_word + " "
                while s[i-1] == " ":
                    i = i-1
            
                current_word = ""
            else:  
                current_word = s[i]+current_word
                print(current_word)

            i-=1

        result = result + current_word

        
        return result 


        