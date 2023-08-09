"""   
You can make functions complex by using if-statements 
and loops within them. Look at the following examples:

"""

# Example 1:

shape1 = [25, 10, "square"]
shape2 = [10, 5, "triangle"]

# function that expects a list argument
def calculate_area(shape):
    
    # if the 3rd value of the list is square,
    # do a square calculation
    if shape[2] == "square":
        area = shape[0] * shape[1]
        
    # if it's a triangle, do a different area
    # calculation
    elif shape[2] == "triangle":
        area = (1/2) * shape[0] * shape[1]
    
    return area

# print the different areas
print(f"Area of shape 1: {calculate_area(shape1)}")        
print(f"Area of shape 2: {calculate_area(shape2)}")





# Example 2:

student_A = {"math": 80, "science": 87, "english": 76}

def grade_average(student_grades):
    total = 0 
    
    # iterate over dictionary of student's grades
    for subjects in student_grades:
        # using "subjects", index over dictionary 
        # and add to total
        total += student_A[subjects]
    
    #compute average
    average = total / len(student_grades)
    
    return average

print(grade_average(student_A))


"""    

Although functions are useful in these examples, 
another concept called, "Objected Oriented Programming"
can make these examples significantly more organized. 
This will be further explained in module 6, so stay tuned!

"""