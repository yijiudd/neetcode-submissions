class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dic={}
        for s in strs :
            str_sorted="".join(sorted(s)) 
            if str_dic.get(str_sorted)!=None:
                str_dic[str_sorted].append(s)
            else :
                str_dic[str_sorted]=[s]
        return list(str_dic.values())   