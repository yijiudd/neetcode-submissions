class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums.sort()
        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                res=num+nums[l]+nums[r]
                if res>0:
                    r-=1
                elif res<0:
                    l+=1
                else:
                    arr.append([num,nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
        return arr
               



    
        