from typing import List, Any
import create2DArray_initializing

def display2DArray_forLoop_1(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Double for loop print using index.")
    for row_index in range(0, len_row):
        for col_index in range(0, len_col):
            print(f"{array[row_index][col_index]} ", end = '')

        print()

def display2DArray_forLoop_2(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Double for loop that extract the row and val, then use \"print\" to display.")
    for row_index in range(0, len_row):
        row = array[row_index]
        
        for col_index in range(0, len_col):
            print(f"{row[col_index]} ", end = '')

        print()

if __name__ == "__main__":
    sample2Darray = create2DArray_initializing.create2DArray_1()

    print()
    display2DArray_forLoop_1(sample2Darray)

    print()
    display2DArray_forLoop_2(sample2Darray)