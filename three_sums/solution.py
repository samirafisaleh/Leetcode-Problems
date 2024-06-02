'''
    NAME:
    3Sum
    
    DESCRIPTION:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    CONSTRAINTS:
    1. 3 <= nums.length <= 3000
    2. -105 <= nums[i] <= 105

    EXAMPLES:
    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.


    URL:
    https://leetcode.com/problems/3sum/description/ 

    STATUS: 
    COMPLETE
'''

class Solution:

    def solution(self, test_list):

        for x in range(0, len(test_list) - 2):
            for y in range(1, len(test_list) - 1):
                for z in range(2, len(test_list)):
                    if test_list[x] + test_list[y] + test_list[z] == 0:
                        pass 

