user_input = input("camelCase: ")
snake_case = ""
for i in range(len(user_input)):
    if i+1 < len(user_input) and user_input[i+1].isupper():
        snake_case += user_input[i].lower() + "_"
    else:
        snake_case += user_input[i].lower()
print("snake_case: " + snake_case)