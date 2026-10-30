class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        stack = [s[0]]

        for i in range(1,len(s)):
            if len(stack)>0:
                ele = stack[-1]

                if ele == "(" and s[i] == ")":
                    stack.pop()
                elif ele == "{" and s[i] == "}":
                    stack.pop()
                elif ele == "[" and s[i] == "]":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        
        if len(stack)==0:
            return True
        
        return False
        
    






            
        