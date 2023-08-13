""" 
Decisions are an integral part of our and daily life. 

For example: if it's raining outside, then we should take
our umbrella; if the food doesn't smell good, don't eat it!

Computers and programming languages work the same way! 

If we have a condition...
        --> then do the following!

Example 1: 
Let's say we want to take a walk outside and pack things
according to the weather. IF it is hot, we should add 
a hat and bottle to our backpack (saved in list). Otherwise,
don't bring anything!

""" 

weather = "hot"
backpack = []

#check if it's hot, then add the items to our list
if weather == "hot":
    backpack.append("hat")
    backpack.append("bottle")
    
else:
    print("bring nothing!") 
    
print(backpack) #--> [hat, bottle]






# Now what happens when it's cold? We obviously want to bring some
# gloves and a scarf. But with the code above, if you change the weather
# variable from hot to cold, the contents of our bag will be empty! 
# We can modify the code by adding an ELIF statement that checks first if the weather is 
# hot, then if it's cold:


weather = "cold"
backpack = []

if weather == "hot":
    backpack.append("hat")
    backpack.append("bottle")
    
elif weather == "cold":
    backpack.append("gloves")
    backpack.append("scarf")
    
else:
    print("bring nothing!")  
    
print(backpack) #--> [gloves, scarf]


"""

Closing Thoughts

1. In the code above, what happens if "cold" was checked first? What does that change?
2. Try adding something to the else statement. Instead of bringing nothing maybe add 
   something else to the backpack.

"""