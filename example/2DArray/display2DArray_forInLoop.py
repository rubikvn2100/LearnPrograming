from typing import List, Any
import create2DArray_initializing

def display2DArray_forInLoop_1(array: List[List[Any]]):  
    print("Double for loop to extract the val, then use \"print\" to display.")
    for row in array:
        for val in row:
            print(f"{val} ", end = '')

        print()

def display2DArray_forInLoop_2(array: List[List[Any]]):
    print("For loop to extract the row and val, then use \"print\" to display the row.")
    for row in array:
        print(row)

if __name__ == "__main__":
    sample2Darray = create2DArray_initializing.create2DArray_1()

    print()
    display2DArray_forInLoop_1(sample2Darray)

    print()
    display2DArray_forInLoop_2(sample2Darray)