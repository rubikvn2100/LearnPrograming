from typing import List, Any
import display2DArray_forInLoop
import create2DArray_initializing

def traverse2DArray_mainDiagonal_1(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Traverse 2D Array main diagonal using while loop.")
    k = len_row - 1
    while k > 0:
        row_index = k
        col_index = 0
        while row_index < len_row and col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1
            col_index += 1

        print()

        k -= 1

    k = 0
    while k < len_col:
        row_index = 0
        col_index = k
        while row_index < len_row and col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1
            col_index += 1

        print()

        k += 1

def traverse2DArray_mainDiagonal_2(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])

    def traverse2DArray_mainDiagonal_helper(row_index , col_index):
        while row_index < len_row and col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1
            col_index += 1

        print()
    
    print("Traverse 2D Array main diagonal using helper function.")
    k = len_row - 1
    while k > 0:
        traverse2DArray_mainDiagonal_helper(k, 0)
        
        k -= 1

    k = 0
    while k < len_col:
        traverse2DArray_mainDiagonal_helper(0, k)

        k += 1

def traverse2DArray_mainDiagonal_3(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])

    def traverse2DArray_mainDiagonal_helper(row_index , col_index):
        while row_index < len_row and col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1
            col_index += 1

        print()
    
    print("Traverse 2D Array main diagonal using helper function and for loop.")
    for k in range(len_row - 1, 0, -1):
        traverse2DArray_mainDiagonal_helper(k, 0)

    for k in range(0, len_col):
        traverse2DArray_mainDiagonal_helper(0, k)

if __name__ == "__main__":
    print()
    sample2Darray = create2DArray_initializing.create2DArray_1()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)

    print()
    traverse2DArray_mainDiagonal_1(sample2Darray)

    print()
    traverse2DArray_mainDiagonal_2(sample2Darray)

    print()
    traverse2DArray_mainDiagonal_3(sample2Darray)