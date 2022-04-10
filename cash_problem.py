# CS50 problem-set 1 "Cash" question
def calculate_cents():
    x: int = 0
    cents = input("Change owed: ")
    if cents == int:
        while cents >= 25:
            x = x + 1
            cents = cents - 25
        while cents >= 10:
            x = x + 1
            cents = cents - 10
        while cents >= 5:
            x = x + 1
            cents = cents - 5
        while cents >= 1:
            x = x + 1
            cents = cents - 1
    elif cents != int:
        cents = input("Change owed: ")
    # Sum coins
    print(x)


calculate_cents()
