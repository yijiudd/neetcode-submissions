class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq={}
        l,r=0,0
        max_freq=0
        while r < len(s):
            char_freq[s[r]]=char_freq.get(s[r],0)+1
            max_freq=max(max(char_freq.values()),max_freq)
            r+=1
            while r-l-max_freq>k:
                char_freq[s[l]]-=1
                l+=1
        return r-l
        