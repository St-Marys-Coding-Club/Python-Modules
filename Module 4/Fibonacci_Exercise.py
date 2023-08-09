"""    
Here's an interesting task: can you generate 
the n-th term of the Fibonacci sequence?

Think hard about what you need to loop and 
define. Do you think you can do it?

P.S.
You can use pythons, "input()" function. However,
it saves the user's input in a string, therefore you 
need might need to convert it to an integer. 

Below is my solution/answer; do you think you can create it in 
less lines of code?

"""


current_number = 1
previous_number = 0


nth_number = int(input("Enter the n-th number you would like: "))

for term in range(nth_number):
    # remember that computers start counting at 0 first
    term += 1
    print(f"term {term}")
    
    if term == 1:
        print(0)
        
    elif term == 2:
        print(1)
             
    # if they are asking for the 3rd term 
    else:
        # the new number should be the sum of the current and previous
        new_number = current_number + previous_number
        
        # then, we re-define what are the current and previous numbers
        previous_number = current_number
        current_number = new_number   
        print(new_number)
        