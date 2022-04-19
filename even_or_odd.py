def even_or_odd(number):
    if number % 2 == 0:  # check if number can be divided evenly by 2
        return print("Even")  # if so, print "even"
    else:
        return print("Odd")  # if not, print "odd"


even_or_odd(2)  # should be even
even_or_odd(3)  # should be odd
even_or_odd(4)  # should be even
