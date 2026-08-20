def remove_fourth_character(word: str) -> str:
    message1 = word[:3]
    message2 = word[4:]
    return message1 + message2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
