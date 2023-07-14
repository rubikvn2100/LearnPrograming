from typing import List, Any
import display2DArray_forInLoop
import create2DArray_initializing

def traverse2DArray_1(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("traverse 2D Array row by row, col by col.")
    row_index = 0
    while row_index < len_row:
        col_index = 0
        while col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')

            col_index +=1

        row_index += 1

    print()

def traverse2DArray_2(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("traverse 2D Array col by col, row by row.")
    col_index = 0
    while col_index < len_col:
        row_index = 0
        while row_index < len_row:
            print(f"{array[row_index][col_index]} ", end = '')

            row_index +=1

        col_index += 1

    print()

if __name__ == "__main__":
    print()
    sample2Darray = create2DArray_initializing.create2DArray_1()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)

    print()
    traverse2DArray_1(sample2Darray)

    print()
    traverse2DArray_2(sample2Darray)