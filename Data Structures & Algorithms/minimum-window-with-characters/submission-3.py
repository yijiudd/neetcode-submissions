class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        have=0
        t_dic={}
        w_dic={}
        res=''
        short_len=float('inf')
        start_i=-1
        for char in t:
            t_dic[char]=t_dic.get(char,0)+1
        need=len(t_dic)
        l=0
        r=0
        while r<len(s):
            w_dic[s[r]]=w_dic.get(s[r],0)+1
            if s[r] in t_dic and w_dic[s[r]]==t_dic[s[r]]:
                have+=1
            while have==need:
                if r-l+1<short_len:
                    short_len=r-l+1
                    start_i=l
                w_dic[s[l]]-=1
                if s[l] in t_dic and w_dic[s[l]]<t_dic[s[l]]:
                    have-=1
                l+=1
            r+=1
        return "" if start_i==-1  else s[start_i:start_i+short_len]

        

        