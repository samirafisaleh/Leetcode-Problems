'''
    NAME:
    Palindrome Number
    
    DESCRIPTION:
    Given an integer x, return true if x is a palindrome , and false otherwise.

    CONSTRAINTS:
    1. -231 <= x <= 231 - 1

    EXAMPLES:
    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
    URL:
    https://leetcode.com/problems/palindrome-number/

    STATUS:
    COMPLETE
'''

import math 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        val = x 
        hashmap = {}

        # All negatives are False
        if val < 0:
            return False

        # Continue iterating until loop reaches below single digit
        while val > 10:
            
            # Calculate the current 10nth (10, 100, 1000, etc.)
            # This gives the "number" of nth. 1000 = 3, 100 = 2, 10 = 1, etc.
            exp = math.floor(math.log(val)/math.log(10))
            y = 10**exp

            # Use hashmap to maintain the current "count" of the 100nth.
            # This will take each digit in the value and place them in the list
            # using the key as the 100nth and the value as the count
            if val > y:
                
                hashmap[y] = 1 if y not in hashmap else hashmap[y] + 1
                val = val - y

        # Append the single's digit
        hashmap[1] = val
        
        # Cover the values in the hashmap to a list
        listresult = list(hashmap.values())

        # Determine whether it's a palindrome
        return listresult == listresult[::-1]



solution = Solution()

tests = [10, 101, 103, 302, 2203, -12, 32, 6006, 12344321]

for test in tests:
    result = solution.isPalindrome(test)
    print(f"Is {test} a palindrome: {result}")




