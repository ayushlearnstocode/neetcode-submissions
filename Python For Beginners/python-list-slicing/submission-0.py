from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    length = len(my_list) - 4
   # return my_list[length - 4::]
    el1 = [my_list[-1]]
    el2 = [my_list[-2]]
    el3 = [my_list[-3]]
    listt = [el3 + el2 + el1]
    return el3 + el2 + el1
    #return listt[]

# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
