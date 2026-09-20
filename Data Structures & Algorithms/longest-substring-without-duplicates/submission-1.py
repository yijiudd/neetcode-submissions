class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j = 0
        max_len=0
        win = set()
        while j < len(s):
            while  s[j] in win:
                win.remove(s[i])
                i += 1
            win.add(s[j])
            max_len=max(max_len,j-i+1)
            j += 1
            
        return max_len
