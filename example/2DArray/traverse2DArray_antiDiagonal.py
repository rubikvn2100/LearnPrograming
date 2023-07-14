from typing import List, Any
import display2DArray_forInLoop
import create2DArray_initializing

def traverse2DArray_antiDiagonal_1(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Traverse 2D Array anti diagonal using while loop.")
    end_sum = len_row + len_col - 1
    sum = 0
    while sum < end_sum:
        row_index = 0 if sum < len_col else sum - len_col + 1 
        while row_index < len_row:
            col_index = sum - row_index
            if col_index < 0:
                break

            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1

        print()

        sum += 1

def traverse2DArray_antiDiagonal_2(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Traverse 2D Array anti diagonal using for loop.")
    end_sum = len_row + len_col - 1
    for sum in range(0, end_sum):
        start_index = 0 if sum < len_col else sum - len_col + 1 
        for row_index in range(start_index, len_row):
            col_index = sum - row_index
            if col_index < 0:
                break

            print(f"{array[row_index][col_index]} ", end = '')
            
            row_index += 1

        print()

if __name__ == "__main__":
    print()
    sample2Darray = create2DArray_initializing.create2DArray_1()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)

    print()
    traverse2DArray_antiDiagonal_1(sample2Darray)

    print()
    traverse2DArray_antiDiagonal_2(sample2Darray)