class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        # Start with the base case
        s = "1"
        
        for _ in range(n - 1):
            curr = ""
            count = 1
            
            # Generate next sequence based on previous
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    curr += str(count) + s[i - 1]
                    count = 1
            
            # Add the last group
            curr += str(count) + s[-1]
            s = curr
        
        return s

        
