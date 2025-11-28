class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            nums.append(nums[i])
        return nums

