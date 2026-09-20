class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr_1d=[]
        for arr in matrix:
            arr_1d+=arr
            def binary_search(l,r,target,nums):
                if l>r:
                    return False
                m=(l+r)//2
                if nums[m]==target:
                    return True
                elif nums[m]>target:
                    return binary_search(l,m-1,target,nums)   
                else:
                    return binary_search(m+1,r,target,nums)
        return binary_search(0,len(arr_1d)-1,target,arr_1d)

        