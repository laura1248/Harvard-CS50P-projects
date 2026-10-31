operators = ["/", "*", "+", "-"]
user_input = input("Expression:  ")
user_input = user_input.replace(" ", "")

def evaluate(expression, operator):
    for i in range(len(expression)-1):
        if expression[i] == operator:
            print(expression[i-1:i+2])
            expression = expression[:i-1] + str(int(eval(expression[i-1:i+2]))) + expression[i+2:]
            print(expression)
            print(len(expression))
            return expression

for operator in operators:
    for i in range(len(user_input)):
        result = 0
        result = evaluate(user_input, operator)
        if result:
            print("Result:", result)
            user_input = result

print(user_input)