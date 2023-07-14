from typing import List, Any
import display2DArray_forInLoop

def min2DArray_1(array: List[List[Any]]) -> Any:
    len_row = len(array)
    len_col = len(array[0])
    
    min_val = array[0][0]
    row_index = 0
    while row_index < len_row:
        col_index = 0
        while col_index < len_col:
            val = array[row_index][col_index]
            if val < min_val:
                min_val = val

            col_index +=1

        row_index += 1

    return min_val

def min2DArray_2(array: List[List[Any]]) -> Any:
    len_row = len(array)
    len_col = len(array[0])
    
    min_val = array[0][0]
    row_index = 0
    while row_index < len_row:
        row = array[row_index]

        val_index = 0
        while val_index < len_col:
            val = row[val_index]
            if val < min_val:
                min_val = val

            val_index +=1

        row_index += 1

    return min_val

def min2DArray_3(array: List[List[Any]]) -> Any:
    len_row = len(array)
    len_col = len(array[0])
    
    min_val = array[0][0]
    for row_index in range(len_row):
        for col_index in range(len_col):
            val = array[row_index][col_index]
            if val < min_val:
                min_val = val

    return min_val

def min2DArray_4(array: List[List[Any]]) -> Any:
    len_row = len(array)
    len_col = len(array[0])
    
    min_val = array[0][0]
    for row in array:
        for val in row:
            if val < min_val:
                min_val = val

    return min_val

if __name__ == "__main__":
    print()
    sample2Darray = [
        [18, 73, 35, 34, 91],
        [94, 25, 64, 97, 11],
        [72, 10, 15, 79, 64]
    ]
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)

    print()
    print(f"Minimum val of array is {min2DArray_1(sample2Darray)}")
    print(f"Minimum val of array is {min2DArray_2(sample2Darray)}")
    print(f"Minimum val of array is {min2DArray_3(sample2Darray)}")
    print(f"Minimum val of array is {min2DArray_4(sample2Darray)}")