"""
Given a partially completed 9x9 Sudoku board, determine if the current state of the board adheres to the rules of the game:
- Each row and column must contain unique numbers between 1 and 9, or be empty (represented as 0).
- Each of the nine 3x3 subgrids that compose the grid must contain unique numbers between 1 and 9, or be empty.
Note: You are asked to determine whether the current state of the board is valid given these rules, not whether the board is solvable.

Constraint:
* Assume each integer on the board falls in the range of [0, 9].
"""

from typing import List

def solution(matrix:List[List[int]]) -> bool:
    """
    thsoudu -> supposing that list are row-wise 
    """
    unique_columns = dict()
    for row in matrix:
        unique_rows = set()
        for index, row_element in enumerate(row):
            if row_element in unique_rows:
                return False
            elif (row_element > 0):
                unique_rows.add(row_element)
                if index in unique_columns:
                    if row_element in unique_columns[index]:
                        return False
                    else:
                        unique_columns[index].add(row_element)
                else:
                    unique_columns[index] = set()
                    unique_columns[index].add(row_element)
    return True


# thsoudu after some study

def solution(matrix:List[List[int]]) -> bool:
    row_check = [set() for _ in range(9)]
    column_check = [set() for _ in range(9)]
    subgrid_check = [[set() for _ in range(3)] for _ in range(3)]
    for row_index in range(9):
        for col_index in range(9):
            element = matrix[row_index][col_index]
            if element > 0:
                if element in row_check[row_index]:
                    return False
                elif element in column_check[col_index]:
                    return False
                elif element in subgrid_check[row_index//3][col_index//3]:
                    return False
                row_check[row_index].add(element)
                column_check[col_index].add(element)
                subgrid_check[row_index//3][col_index//3].add(element)
    return True