# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.


# Example 1:

# Input: nums = [3,2,1,4]
# Output: 2


# Example 2:

# Input: nums = [1,2]
# Output: -1

class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        if len(nums) < 3:
            return -1
        else:
            return nums[1]