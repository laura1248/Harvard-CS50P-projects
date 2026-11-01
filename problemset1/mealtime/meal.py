
def main():
    user_input = input("What time is it? ")
    user_input = convert(user_input)
    if 7 <= user_input <= 8:
        print("breakfast time")
    elif 12 <= user_input <= 13:
        print("lunch time")
    elif 18 <= user_input <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time[:4].split(":"))
    if time.endswith("p.m."): 
        hours += 12
    return hours + minutes / 60


if __name__ == "__main__":
    main()