from typing import List, Any
import display2DArray_forInLoop

def create2DArray_1() -> List[List[Any]]:
    sample2DArray = [
        ["aa", "ab", "ac", "ad", "ae"],
        ["ba", "bb", "bc", "bd", "be"],
        ["ca", "cb", "cc", "cd", "ce"]
    ]

    return sample2DArray

def create2DArray_2() -> List[List[Any]]:
    row0 = ["aa", "ab", "ac", "ad", "ae"]
    row1 = ["ba", "bb", "bc", "bd", "be"]
    row2 = ["ca", "cb", "cc", "cd", "ce"]

    sample2DArray = [row0, row1, row2]

    return sample2DArray

def create2DArray_3() -> List[List[Any]]:
    sample2DArray = []
    for first_char in ['a', 'b', 'c']:
        row = []
        for second_char in ['a', 'b', 'c', 'd', 'e']:
            row.append(first_char + second_char)
        
        sample2DArray.append(row)

    return sample2DArray

def create2DArray_4() -> List[List[Any]]:
    sample2DArray = [[x + y for y in ['a', 'b', 'c', 'd', 'e']] for x in ['a', 'b', 'c']]

    return sample2DArray

if __name__ == "__main__":
    print()
    sample2Darray = create2DArray_1()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)
    
    print()
    sample2Darray = create2DArray_2()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)
    
    print()
    sample2Darray = create2DArray_3()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)
    
    print()
    sample2Darray = create2DArray_4()
    display2DArray_forInLoop.display2DArray_forInLoop_1(sample2Darray)