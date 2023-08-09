"""  

Now let's say we only like going out when the temperature outdoors 
is less than 18 degrees celcius. Addtionally, we only like it when there is no 
rain or snow. Therefore, how can we check both statements? 

Well, if we are looking if two statements are TRUE, then we can use,
"and" in our if statements!

"""


temperature_celcius = 17
weather = "clear skies"

# Here, I used "<". You can also use "<=" to check if it's also equals 18
# See decision operators table in this repository for details!
if weather == "clear skies" and temperature_celcius < 18:
    print("let's take a walk!")
else:
    print("don't take a walk!")
    






# Now, let's say we only take walks when the temperature is between the range of 
# 18'C and 10'C? We can change the code by checking the temperature first, then only if the temperature's
# ideal, check the weather. This adds a level of priority to our program and is called, "nesting".

temperature_celcius = 18
weather = "clear skies"
    
if temperature_celcius < 19 and temperature_celcius > 10:
    if weather == "clear skies":  
        print("let's take a walk!")
else:
    print("don't take a walk!")
    
    
      
    
    
    
    
# However, since many of us are in school, we only like to take walks during a Saturday OR a Sunday
# To check as long as one of the statements is true, we can use the the "or" operator. For
# this example, let's ignore the temperature for now. 

temperature_celcius = 18
current_day = "Monday"
weather = "clear skies"
    
if current_day == "Saturday" or current_day == "Sunday":
    if weather == "clear skies":  
            print("let's take a walk!")
else:
    print("don't take a walk!")
    


"""

Closing Thoughts

1. Check the comparion and logic operator images located in this repository. Can you incorporate them 
   in the code above to check other things?
   
2. Although nesting if statements can be good, what is a big disadvantage if we have too many?

"""