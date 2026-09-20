class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=0
        res=[]
        d_q=collections.deque()
        while r < len(nums):
            while d_q and nums[d_q[-1]]<nums[r]:
                d_q.pop()
            d_q.append(r)

            if l >d_q[0]:
                d_q.popleft()
            
            if r >= k -1:
                res.append(nums[d_q[0]])
                l += 1
            r += 1
        return res
