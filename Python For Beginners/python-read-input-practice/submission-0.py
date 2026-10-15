def add_two_numbers() -> int:
    user_input = input()
    user_list = user_input.split(",")
    num1 = int(user_list[0])
    num2 = int(user_list[1])
    total = num1 + num2
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
