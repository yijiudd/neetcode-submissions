class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            s1_dic={}
            win_dic={}
            for char in s1:
                s1_dic[char]=s1_dic.get(char,0)+1
            l=0
            r=0
            while r < len(s2):
                win_dic[s2[r]]=win_dic.get(s2[r],0)+1
                
                while r-l>=len(s1):
                    win_dic[s2[l]]-=1
                    if win_dic[s2[l]]==0:
                        del win_dic[s2[l]]
                    l+=1
                if win_dic==s1_dic:
                    return True
                r+=1
            return False
    

        
        