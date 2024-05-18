'''
    NAME:
    Valid Sudoku
    
    DESCRIPTION:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


    CONSTRAINTS:
    1. board.length == 9
    2. board[i].length == 9
    3. board[i][j] is a digit 1-9 or '.'.

    EXAMPLES:
    Example 1:
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
        
    URL:
    https://leetcode.com/problems/valid-sudoku/description/

    STATUS:
    COMPLETE
'''

class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isduplicate(hashmap):
            for itm in hashmap.values():
                if itm > 1:
                    return False 
                
            return True 
        
        def initialize_hashmap():
            return {
                "1" : 0,
                "2" : 0,
                "3" : 0,
                "4" : 0,
                "5" : 0,
                "6" : 0,
                "7" : 0,
                "8" : 0,
                "9" : 0
            }

        def threebythree(topleft):
            hashmap = initialize_hashmap()

            for idx in range(0, 3):
                for idy in range(0, 3):

                    val = board[topleft[1] + idy][topleft[0] + idx]

                    if val != ".":
                        hashmap[val] = 1 if val not in hashmap else hashmap[val] + 1

            return isduplicate(hashmap)

        def perrow(row):
            hashmap = initialize_hashmap()

            for val in row:
                if val != ".":
                    hashmap[val] = 1 if val not in hashmap else hashmap[val] + 1

            return isduplicate(hashmap)

        def percol(col):
            hashmap = initialize_hashmap()

            for row in range(0, 9):
                val = board[row][col]
                if val != ".":
                    hashmap[val] = 1 if val not in hashmap else hashmap[val] + 1
            
            return isduplicate(hashmap)


        final = True 
        for idx in range(0, 9, 3):
            for idy in range(0, 9, 3):
                final = final and threebythree((idx, idy))

        for row in board:
            final = final and perrow(row)

        for idx in range(0, 9):
            final = final and percol(idx)

        print(f"Is Sudoku Valid: {final}")


solution = Solution()

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


result = solution.isValidSudoku(board)
    




