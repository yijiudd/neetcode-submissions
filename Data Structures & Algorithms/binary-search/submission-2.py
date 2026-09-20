class Solution:
    def search(self, nums: List[int], target: int) -> int:
 
        def binary_search(l,r,target):
            m=(l+r)//2
            if l>=r and nums[m]!=target:
                return -1
            if nums[m]==target:
                return m
            elif nums[m]>target:
                return binary_search(l,m,target)
            else:
                return binary_search(m+1,r,target)
        return binary_search(0,len(nums)-1,target)



        