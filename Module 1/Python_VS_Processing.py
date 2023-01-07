'''
In Processing, we use semi colons and brackets. 

In Python we don't. Instead we use indents and colons!

For example...
'''

# Variables | Module 2
integer = 1
float = 20.0
boolean = True
string = "Wow!"

# Function
print("Hello world!")


# If Statement | Module 
my_variable = 123
if my_variable > 100:
    # Conditonal Statments | Module 
    if my_variable > 100 and my_variable < 110: # Instead of && and || we explicitly just say the word. (&& -> and) (|| -> or)
        print("Variable is greater than 100 but less than 110")
    elif my_variable >= 110 or my_variable == 123:
        print("Variable is greater than or equal to 110! or it equals 123! 😮")
    else:
        print("Variable is greater than 100!")

# Switch Case (New in Python 3.10, but not in programming.) It's like a If statement. | Better explained in Module 3
match my_variable:
    case 123:
        print("The variable's value is 123.")

    case 100:
        print("The variables value is 100.")

    case _:
            print("The variables value wasn't one that was listed.")


# For Loop
my_list = [123, 20, True, "What? Multiple Types???"]
for x in my_list:
    print(type(x)) # Outputs the type each item in the list is. (eg. 123 -> int)


# While Loop
my_counter = 0
while my_counter < 10:
    my_counter += 1 # add one to counter
    print("Hello, " + str(x) + " times!") # We have to convert the variable x into a string or we will get an error!


# Class
class MyClass:
    def __init__(self, _myValue):
        self.myValue = _myValue

    def MyClass_Function(self):
        print(self.myValue)

    @staticmethod
    def MyClass_StaticFunction():
        print("Wow, a static function!")



'''
In the coming modules, we will go over each example in this file.

So if you don't understand or even know what you are looking at,

Do not fret!
'''