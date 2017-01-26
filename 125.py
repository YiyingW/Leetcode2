class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1:
            return True
        l, r = 0, len(s)-1
        while l <= r:
            print l, r
            while not s[l].isalnum() and l < r:
                l += 1
            while not str(s[r]).isalnum() and l< r:
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
