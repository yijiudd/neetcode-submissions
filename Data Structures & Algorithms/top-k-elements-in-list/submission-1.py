class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        sorted_dic= dict(sorted(dic.items(), key=lambda x:x[1],reverse=True))
        return list(sorted_dic.keys())[:k]

        
        