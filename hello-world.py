# Objective: Define a variable and create a prompt that asks for a users name, then says hello "Name".
# Goals: If possible, continue to create programs primarily with Pseudo-Code first, and then enhance them by creating
# a functioning testing environment. Perhaps begin including Object Oriented Programming as well? And also...
# To begin, begin. Then create a function that takes in two arguments, "self, name" hello.
# def greet(name: str):
#     # Ask the user for their name... and then... mm... Never give up!
#     name_answer: str = input(f"Hello, World!, What is your name, user {name}? ")
#     print(f"Hello {name_answer}, it's so nice to meet you!")  # Print out the  coordinating greeting message
#
# if __name__ == '__main__':
#     greet('PyCharm')

# Let's now try some object oriented programming, again...
# Never give up...

class User:
    """Properties"""
    # Class variables
    name: str = None
    age: int = 0
    bio: str = None

    def __init__(self, name, age, bio):
        # Let's define some class attributes that will help us to
        # get to know our user a bit better.
        self.name = name
        self.age = age
        self.bio = bio

        print(f"Hello {name}, nice to meet you!")
        print(f"I see you are {age} years old")
        print(f"Here is your Bio: {bio}")


answer_1 = input("What is your name, new user?")
answer_2: int = int(input("How old are you?"))
answer_3 = input("Please tell me a bit about yourself...")

# In general...
User(answer_1, int(answer_2), answer_3)


class Stats:
    """Properties"""
    # Class variables
    food: str = None
    coins: int = 0
    exp: int = 0
    class: str = "Shepherd"

    def __int__(self, food, coins, exp):
        self.food = food
        self.coins = coins
        self.exp = exp
        
# Current practice and problems being worked on. (Currently: Codewars)
def series_sum(n: int):
    series: float = 1 / 4
    if n == 1:
        return print(1)
    elif n == 2:
        return print(1 + series)
    elif n > 1:
        series = 1 / (4 + 1 * series)
        return print(1 + series)


series_sum(1)
series_sum(2)
series_sum(5)

# Practice
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Object Oriented/Classes
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
