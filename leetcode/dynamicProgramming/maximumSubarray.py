# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide
# and conquer approach, which is more subtle.
from sys import maxsize


class Solution:
    def maxSubArray(self, nums):
        max_ending_here = 0
        max_so_far = - maxsize - 1

        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
