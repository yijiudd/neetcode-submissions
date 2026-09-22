class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.track=[]
        def dfs(choices,start,target):
            if target<0:
                return 
            if target==0:
                self.res.append([*self.track])
                return
            for i in range(start,len(choices)):
                self.track.append(choices[i])
                dfs(choices,i,target-choices[i])
                self.track.pop()
        dfs(nums,0,target)
        return self.res



        