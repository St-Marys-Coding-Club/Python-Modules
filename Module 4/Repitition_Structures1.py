"""     
When you're going to develop projects of your own,
there's bound to lines of code that are repetitive.
For example, like drawing a circle 10 or 20 times (we'll get
into this in the later modules). 

Instead of writing the same line 20 times, you could create a 
FOR-LOOP to accomplish this:

For 20 times...
    ---> do this

"""

# To create a for-loop, we need to iterate over a certain a range 
# of numbers or a datatype (list, string, dictionary, etc). To print the first 
# 10 numbers, we use "i" to iterate over the range from 0-9 (because we always start at 0 in programming)

for i in range(10):
    print(i)
    
    
# "i" is simply a placeholder, we can also change it to "number" or whatever we want:
for number in range(10):
    print(number)
    

    
# Since we know it loops 10 times, how about we add 2 to my_num each time?
my_num = 6
for i in range(10):
    my_num += 2
print(my_num)


# Another interesting property is that for-loops can be used to iterate over a list. 
# Instead of looping in a certain range(x), we can substitute it with what we want to iterate over:

coding_club = ["Jyle", "Adrian", "Justin"]
for members in coding_club:
    print("Mr. " +  members) 
