# [1, 4, 5, 6, 12, 13] k = 3
# [0, 3, 5, 8, 32, 37]
# [0, 3, 4, 5, 11, 12]
# thoughts:
# - can't greedily take least different numbers because of above ex
# - DP?
# - need O(nlogn) approach
# - prefix sum + sliding window
# [1, 4, 8, 13]
# [0, 3, ]

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        curr_max = 1
        curr_sum = 0
        nums.sort()
        print(nums)
        for r in range(0, len(nums)):
            diff = nums[r] - nums[r-1]
            curr_sum += (r - l) * diff
            while l < r and curr_sum > k:
                curr_sum -= (nums[r] - nums[l])
                l += 1
            curr_max = max(curr_max, (r-l) + 1)
        
        return curr_max

        

