class Solution(object):
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Isomorphic == each char maps to another char, no varying mappings allowed
        
        # EX 1: "add" and "egg" -> true
        # EX 2: "foo" and "bar" -> false 
        
        # make a empty dictionary of mappings
        Dict = {}
       
        for i in range(len(s)):
            
            # if key is already existent -> fetch existing val and compare to t[i]
            if s[i] in Dict:
                if Dict[s[i]] != t[i]:
                    # if you use the key and a diff val comes, its false
                    return False

            # cont to add if False was not encountered
            Dict[s[i]] = t[i]
               
        
        # now flip keys and values to check other side
        rever_dict = dict([(value, key) for key, value in Dict.items()])
        
        # if flipped w duplicate keys -> no duplicate keys can exist -> will reduce length of new dictionary
        if len(rever_dict) != len(Dict):
            return False
    
        return True 
    
