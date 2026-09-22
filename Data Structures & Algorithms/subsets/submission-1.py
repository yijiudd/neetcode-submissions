class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.track=[]
        self.res=[]
        def dfs(choices,i):
    
            for j in range(i,len(choices)):
                self.track.append(choices[j])
                self.res.append(self.track.copy())
                dfs(choices,j+1)
                self.track.pop()
        dfs(nums,0)
        self.res.append([])
        return self.res