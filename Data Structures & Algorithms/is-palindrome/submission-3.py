class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(char.lower() for char in s if char.isalnum())
        if len(s_clean)<=1:return True
        i = 0
        j = len(s_clean)-1
        while s_clean[i] == s_clean[j]:
            i += 1
            j -= 1
            if i >= j:
                return True
        return False
