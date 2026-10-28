user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
accepted_inputs = ["42", "forty-two", "forty two"]
if user_input.lower() in accepted_inputs:
    print("Yes")
else:
    print("No")