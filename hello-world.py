# Objective: Define a variable and create a prompt that asks for a users name, then says hello "Name".
# Goals: If possible, continue to create programs primarily with Pseudo-Code first, and then enhance them by creating
# a functioning testing environment. Perhaps begin including Object Oriented Programming as well?

# To begin, create a function that takes in two arguments, "self, name"

def greet(name: str):
    # Ask the user for their name...
    name_answer: str = input(f"Hello, World!, What is your name, user {name}? ")
    print(f"Hello {name_answer}, it's so nice to meet you!")  # Print out a greeting message


if __name__ == '__main__':
    greet('PyCharm')
