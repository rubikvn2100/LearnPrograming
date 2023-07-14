from typing import List, Any
import create2DArray_initializing

def display2DArray_naivePrint_1(array: List[List[Any]]):
    print("Naive print using \"print\" method to print the whole 2D array.")
    print(array)


def display2DArray_naivePrint_2(array: List[List[Any]]):
    print("Naive print using \"print\" method to print each row in the 2D array.")
    print("Row 0: ", array[0])
    print("Row 1: ", array[1])
    print("Row 2: ", array[2])


def display2DArray_naivePrint_3(array: List[List[Any]]):
    print("Naive print using \"print\" method to print each element in the 2D array.")
    print(array[0][0], array[0][1], array[0][2], array[0][3], array[0][4])
    print(array[1][0], array[1][1], array[1][2], array[1][3], array[1][4])
    print(array[2][0], array[2][1], array[2][2], array[2][3], array[2][4])

if __name__ == "__main__":
    sample2Darray = create2DArray_initializing.create2DArray_1()

    print()
    display2DArray_naivePrint_1(sample2Darray)

    print()
    display2DArray_naivePrint_2(sample2Darray)

    print()
    display2DArray_naivePrint_3(sample2Darray)