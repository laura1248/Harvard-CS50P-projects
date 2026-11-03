amount_due = 50

while amount_due > 0:
    print(f"Amount due: {amount_due}")
    user_input = int(input("Insert coin: "))
    if user_input in [5, 10, 25]:
        amount_due -= user_input

print(f"Change owed: {-amount_due}")