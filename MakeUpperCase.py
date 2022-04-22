def make_upper_case(s: str):
    return print(s.upper())  # Make uppercase

# Alternatively...

def make_upper_case(s: str):
    if type(s) != str:
        return print("Incorrect data type. Please try again.")

    return print(s.upper())  # Make uppercase

make_upper_case('stop')
