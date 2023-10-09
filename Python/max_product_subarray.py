"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize a result variable
        result = nums[0]

        # initialize a max and min prod variable set to index 0
        currMax = nums[0]
        currMin = nums[0]

        # loop from the first ind to end of list
        for i in range(1, len(nums)):
            # if elem is -:
            if nums[i] < 0:
                # swap the max and min prod
                currMax, currMin = currMin, currMax
            # find the currMax between currmax * elem or just elem
            currMax = max(nums[i], nums[i]*currMax)
            # find the currMin between currmin * elem or just elem
            currMin = min(nums[i], nums[i]*currMin)
            # update result to be max of currmax or result
            result = max(result, currMax)

        # return result
        return result
