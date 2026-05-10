class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        # ex: [2, 2, 3, 1]
        # l_ptr = 2
        # r_ptr = 2
        # map = {2: 0, 3: 1}
        # curr_sum = 3
        # sliding window approach
        l_ptr = 0  
        min_subarr_len = float('inf')
        map = {}
        curr_sum = 0
        for r_ptr in range(len(nums)):
            curr_val = nums[r_ptr]
            if map.get(curr_val, 0) == 0:
                map[curr_val] = 0
                curr_sum += curr_val
            map[curr_val] += 1
            while l_ptr <= r_ptr and curr_sum >= k:
                min_subarr_len = min(min_subarr_len, r_ptr - l_ptr + 1)
                l_val = nums[l_ptr]
                l_ptr += 1
                map[l_val] -= 1
                if map[l_val] == 0:
                    curr_sum -= l_val
        if min_subarr_len == float('inf'):
            return -1
        return min_subarr_len
