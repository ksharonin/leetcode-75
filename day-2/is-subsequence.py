class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # base cases
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        
        # initiate indexes
        i, j = 0, 0
        
        # check order & add if s==t appears
        # advance pointers when valid == shows
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        # if matching len -> found correct order
        if i == len(s):
            return True
        else:
            # missing chars or improper order
            return False
