"""  

The previously mentioned for-loops seem quite powerful.
However, their flaw is you can only set them to loop 
for a finite amount -- you have to know before hand
how long they should run for.

Therefore, what can we do when we need a loop to run
indefinitely, like how long a game should be running?

In this case, we need a "WHILE" loop. It works by looping
and checking for a condition everytime it loops. Similar to 
an if-statement, if the condition is true or false, the 
loop stops:


while condition is true...
        ---> do this


"""



# In the simplest example, how much do we need to add to 37 to get to 100?
initial_num = 37
difference = 0

while initial_num < 100:
    #add 1 to our initial_num
    initial_num += 1
    #add 1 to the difference counter
    difference += 1
    
print(difference)



# In this other example, let's print out how many tries it takes the computer
# to guess your number between 1 and 10 by importing the randint function! Remember to define the variable
# before the loop or else it wouldn't know it's checking condition. 
import random
from random import randint

my_num = 6
number_of_tries = 1
computer_guess = -1 #negative number as a placeholder

#as long as the computer's IS NOT equal to my number...
while computer_guess != my_num: 
    #redefine the computer's guess at each loop/try
    computer_guess = randint(1,10)
    #add 1 to tries counter
    number_of_tries = 1 
    
print(f"Tries taken: {number_of_tries}")



# Another example: let's say the coding club has a list of interested students 
# However, we can only accept 5 because of limited resources
# How can we students while checking for the 5-person condition?
# Let's use RECURSION:

coding_club = ["Jyle", "Adrian", "Justin"]
interested_students = ["John", "Adam", "James", "Daisy", "Liz"]
index = 0

while len(coding_club) != 5:
    # we add students based on our current index counter
    coding_club.append(interested_students[index])
    # remember to update, index to move to the next person
    index += 1
print(coding_club)



# While loops can also be used to run a piece of code forever. Basically, make the 
# checking condition always TRUE no matter what!

counter = 0
my_list = []

while True:
    print("hello again!")  
    my_list.append(counter)
    counter += 1 
    
    
# However, if we want to exit the "while True" loop somehow, we can simply use, "break"
# In the following example, let's exit the loop when we say hello the 10th time by using
# an if-statement.  

counter = 0
my_list = []

while True:
    print("hello again!")  
    my_list.append(counter)
    print(my_list)
    counter += 1 
    #checking the value of counter
    if counter == 10:
        break
    