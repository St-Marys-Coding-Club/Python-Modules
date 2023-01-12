'''

Object Oriented Programming is a coding model that 
focuses your programs design around data and objects.

Let's take the following example:
    - We want to create a list of sandwiches.
    - Each sandwich in the list should have their length, bread type and toppings listed.

How would we go about solving this problem?

Well we could...
'''
 

sandwich_1_length = "6 inches"
sandwich_1_bread = "white"
sandwich_1_toppings = ["lettuce", "bacon", "tomato"]

sandwich_2_length = "12 inches"
sandwich_2_bread = "whole grain"
sandwich_2_toppings = ["meatlballs", "cucumber", "cheese"]

'''
This could work, but as you can see, it becomes rather tedious,
and the more sandwiches we make, the more difficult it will become to manage.

And also, it just looks messy.


Instead, we can use classes to create a "Sandwich" class, and use that class to create objects!


But wait, what is a class, and what is an object?

In simplest terms, basically a class is a template for objects. 
'''

class Sandwich:
    def __init__(self, length, bread, toppings):
        self.length = length
        self.bread = bread
        self.toppings = toppings


Sandwich_1 = Sandwich("6 inches", "white", ["lettuce", "bacon", "tomato"])
Sandwich_2 = Sandwich("12 inches", "whole grain", ["meatballs", "cucumber", "cheese"])

"""
Now our code looks more readable!

Our class Sandwhich is our template for our sandwiches, and instead of having to 
manually create a variable for each attribute of our sandwhich, we just make a "Sandwich" object 
and pass the attributes into our constructor. (More info on what this later down.)


Now if we want an attribute of our sandwhich, instead of:
"""

print(sandwich_1_bread)
print(sandwich_2_toppings)


"""
We can now do:
"""

print(Sandwich_1.length)
print(Sandwich_2.toppings)

'''
Creating Sandwich objects also enables us to create a list of Sandwich Objects like so:
'''

Sandwiches = [
    Sandwich("sliced", "white", ["peanut butter", "strawberry jam"]),
    Sandwich("italian herbs", "steak", ["lettuce", "olives", "white cheese", "hot sauce"]),
    Sandwich("white bread", "veggies", ["spinach", "cucumber", "onions"]),
    Sandwich("panini", "chicken", ["lettuce", "hot pepper", "cheddar cheese"])
]

"""
Much cleaner right?

But that's not all we can do, we can add functionality to our classes!


Lets take another example:
    - We want to create a list of car engines
    - Each engine has their type and their fuel economy (amount of L used per 100km [L/100km])
"""
  
class Car_Engine: # type: ignore  | Ignore this comment! :) 
    def __init__(self, enginetype, fuelEconomy):
        self.enginetype = enginetype
        self.fuelEconomy = fuelEconomy

Engines = [Car_Engine("V4", 4), Car_Engine("V6", 10), Car_Engine("V8", 18.7)]

"""
Cool pretty easy. But how do we calculate:
    - How many km can the engine go with X liters of gas?
    or
    - How many liters does the engine use when travelling Y km?

Well, we can manually calculate these values for each engine like this: (Let's say X = 10, Y = 58)
"""

print(10 * (Engines[0].fuelEconomy/100)) # Distance that can be travelled with 10 litres of gas (250)

print((Engines[0].fuelEconomy/100) * 58) # Liters of Gas Consumed with 58 km of travel (2.32)

"""
Sure, it works, however, you wouldn't understand what those lines outputed if it was not commented. 
You would also have to repeat these equations everytime you wanted to get those values.

In contrast, you could also do the problem another way.

Instead of just having attributes in our engine class, we should add some functionality to it.
"""

class Car_Engine:
    def __init__(self, enginetype, fuelEconomy):
        self.enginetype = enginetype
        self.fuelEconomy = fuelEconomy

    
    def Calculate_KM_FOR_LITERS(self, liters):
        return liters / (self.fuelEconomy / 100)

    def Calculate_LITERS_FOR_KM(self, km):
        return (self.fuelEconomy / 100) * km

Engines = [Car_Engine("V4", 4), Car_Engine("V6", 10), Car_Engine("V8", 18.7)] # Redeclaring this or we'll get an error! 

"""
Now, we no longer need to manually calculate each time we need a value,
instead, we can just call our Engine Classes (newly) built-in function!
"""

print(Engines[0].Calculate_KM_FOR_LITERS(10)) # 252.0
print(Engines[0].Calculate_LITERS_FOR_KM(58)) # 2.32


# If we want the whole list:
for x in Engines:
    print("\n" + x.Calculate_KM_FOR_LITERS(10))
    print(x.Calculate_LITERS_FOR_KM(58) + "\n") # Adding escape characters for formatting.

"""
This is just a quick overview of what classes and object orient programming is.

In the coming files, we'll explore each topic more specificly.
"""




    




