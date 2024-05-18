
'''
    Title: Two Sum
    Link: https://leetcode.com/problems/two-sum/description/
'''

'''
    NAME:
    Two Sum
    
    DESCRIPTION:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    CONSTRAINTS:
    1. 2 <= nums.length <= 104
    2. -109 <= nums[i] <= 109
    3. -109 <= target <= 109
    4. Only one valid answer exists.

    EXAMPLES:
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    
    URL:
    https://leetcode.com/problems/two-sum/description/

    STATUS:
    COMPLETE
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        hashmap = {}

        for idx, num in enumerate(nums):
            
            rem = target - num
            print(f"remainder: {rem}")
            if rem in hashmap:
                print("Got em")
                return [idx, hashmap[rem]]
            

            hashmap[num] = idx
            print(hashmap)

        return result
        

solution = Solution()
result = solution.twoSum([2, 3, 1], 5)

print(f"Result: {result}")


