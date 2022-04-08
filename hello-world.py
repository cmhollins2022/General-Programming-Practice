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


# Let's now try some object oriented programming again... in an attempt to get back into the
# basic concepts, and into the swing of things.

class User:
    """Properties"""
    # Class variables
    name: str = None
    age: int = None
    bio: str = None

    def __init__(self, name: str, age: int, bio: str):
        # Let's define some class attributes that will help us to
        # get to know our user a bit better.
        self.name = name
        self.age = age
        self.bio = bio

        def get_name(name_prompt):
            # Prints out cooresponding prompt...
        def get_age(age_prompt):
            # Prints out cooresponding prompt...
        def get_bio(bio_prompt):
            # Prints out cooresponding prompt...


new_user = User("User_1", 0, "Not currently known")
