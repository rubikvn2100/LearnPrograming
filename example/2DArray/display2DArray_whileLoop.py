from typing import List, Any
import create2DArray_initializing

def display2DArray_whileLoop_1(array: List[List[Any]]):
    len_row = len(array)
    len_col = len(array[0])
    
    print("Double while loop print using index.")
    row_index = 0
    while row_index < len_row:
        col_index = 0
        while col_index < len_col:
            print(f"{array[row_index][col_index]} ", end = '')

            col_index +=1

        print()

        row_index += 1

def display2DArray_whileLoop_2(array: List[List[Any]]):
    len_row = len(array)
    
    print("Double while loop to extract the row and then use \"print\" to display the row.")
    row_index = 0
    while row_index < len_row:
        row = array[row_index]
        print(f"row {row_index}: {row}")

        row_index += 1

if __name__ == "__main__":
    sample2Darray = create2DArray_initializing.create2DArray_1()

    print()
    display2DArray_whileLoop_1(sample2Darray)

    print()
    display2DArray_whileLoop_2(sample2Darray)