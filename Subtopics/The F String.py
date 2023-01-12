"""
The f-string is an alternative to formatting strings.
The functionality was added in Python 3.6 and is very useful!

Normally, you would format string like:
"""

x = 100
print("The value of x is: " + str(x) + "!")


# OR

print("The value of x is: %s!" % (x))

# OR

print("The value of x is: {}!".format(x))


"""
Instead, using f-strings, you can format your strings like this:
"""

print(f"The value of x is {x}!")

"""
It's super simple! You can create an f-string by simply putting the letter "f" before
the quotation marks of a string, and to insert a variable you simple type {} and put your variable
inbetween!


However, do note, because of the f string, you cannot use the { or } character seperately. They must
be typed as an escape character. (eg. "\{" or "\}") 


Pretty cool right?
"""


def SomeSuperComplexFunction(input):
    return input + 1

print(f"Your super complicated function returned: {SomeSuperComplexFunction(20)}. ")