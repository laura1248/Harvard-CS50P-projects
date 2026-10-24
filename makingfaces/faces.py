emoji_list = [
    [":)", "🙂"],
    [":(", "🙁"],
    [">:(", "😠"],
    [":o", "😮"]
]

user_input = input()

for emoji in emoji_list:
    user_input = user_input.replace(emoji[0], emoji[1])
print(user_input)