"""   
Although functions are useful, the variables that are defined
inside them cannot be used in the rest of the program.
This is because they are considered LOCAL variables.
Variables defined outside the function can be accessed
everywhere and are called GLOBAL variables:

The scope of a variables is important to consider:

""" 

# the following are global variables since they are defined
# outside of a function -- can be used everywhere
x = 10
y = 20

def addition(num_1, num_2):
    # "sum" is a local variable -- it's defined inside the function
    sum = num_1 + num_2
    return sum

output = addition(x, y)

# this results in an error:
print(sum)

# this does not:
print(output)