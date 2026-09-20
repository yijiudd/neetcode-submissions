class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                start = num
                arr = [start]
                while start + 1 in nums_set:
                    start += 1
                    arr.append(start)
                max_len = max(max_len, len(arr))
        return max_len   