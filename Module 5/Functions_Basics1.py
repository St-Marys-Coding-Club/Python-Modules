""" 

Functions can help us organize our programs.
If we have a specific process that uses many lines
of code, why not shorten it to one statement?

Let's say we want to calculate the area of multiple 
triangles. We can DEFINE a function and re-use it 
multiple times with the different dimensions of triangles.

"""


base1 = 5
length1 = 10

base2 = 2
length2 = 4

# We can define a "calculate area" function that takes two
# arguments. These two arguments can be used as variables within
# the function

def calculate_area(base, length):
    # Create a variable named area
    area = (1/2) * base * length 
    # Return the area as the output of the function. 
    return area

#We can then use our defined function and save it in another variable
triangle1_area = calculate_area(base1, length1)
triangle2_area = calculate_area(base2, length2)

#Format using f-string
print(f"triangle 1 area {triangle1_area}")





# Functions can have no arguments at all. They can also have no 
# "return" if they don't need to return anything. 

def say_hello():
    user_name = input("What is your name? ")
    print(f"Hello, {user_name}!")

#use our function
say_hello()
    