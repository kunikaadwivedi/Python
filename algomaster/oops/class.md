# 1. What is self? (The Identity)

self represents the specific object you are currently dealing with.


Inside the class definition, Python requires self as the very first argument in your functions so the class knows which object's data to modify or read.

# 2. What is __init__? (The Constructor)
The __init__ function is a special, built-in Python method. You can think of it as the initializer or the setup wizard.

The moment you create a new object from a class, Python automatically runs the __init__ function to set up that object's initial characteristics (called attributes).

# 3. What is a CLass & Object/instances
A class is a recipe. An object is a cake baked from that recipe. The recipe doesn't taste like cake, and you can bake many cakes from the same recipe without them sharing icing.

## Note 
That's the whole trick: one function defined once, reused for every instance, with self filling in which instance it should look at.