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

## __bases__
This is a tuple of the classes a class inherits from directly. For a plain class Product:, that tuple contains just object.

# 4.__new__ vs __init__ 
Python actually uses two methods to build an object, not one. __new__ creates the empty instance, and __init__ fills it in. The class call (Product(...)) calls __new__ first, which returns a new (typically empty) object of the class, and then Python passes that object to __init__ as self.

# 5. @classmethod

### The Key Difference: self vs cls

Instance Method: Takes self as its first parameter. It has access to individual object data (like self.name or self.balance).

Class Method: Takes cls as its first parameter. Instead of receiving a specific object, Python automatically passes the entire class into it. This means it can access and modify class-level state, but it cannot see individual object data.