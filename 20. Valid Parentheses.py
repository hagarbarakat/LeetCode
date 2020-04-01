class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] 
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            if s[i] == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            if s[i] == "[":
                stack.append("[")
            if s[i] == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            if s[i] == "{":
                stack.append("{")
            if s[i] == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
        if len(stack) > 0:
            return False
        else:
            return True


#------------------------------------------------------------