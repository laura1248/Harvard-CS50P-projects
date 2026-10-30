extensions = [["gif", "jpg", "jpeg", "png"], ["pdf", "txt", "zip"]]
user_input = input("File name: ")

if user_input.split(".")[-1].lower() in extensions[0]:
    print("image/" + user_input.split(".")[-1].lower())
elif user_input.split(".")[-1].lower() in extensions[1]:
    print("application/" + user_input.split(".")[-1].lower())
else:
    print("application/octet-stream")