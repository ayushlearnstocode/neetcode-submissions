from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = dict()

    for i in word:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict
        




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))


#my_list = ["ayush", 200, "viraj", 2.2, 200 , "ayush", 200]

# my_dict = {
#     "ayush": 2, 
#     200: 3, 
#     "viraj" 1, 
#     2.2 : 1
# }
