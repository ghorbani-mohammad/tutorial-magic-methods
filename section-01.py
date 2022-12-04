# In this section we're going over __new__ function

# Whenever a new object of a class is instantiated __new__ and __init__ methods are called.
# __new__ method will be called when an object is created and __init__ method will be called to initialize the object.
# So in a nutshell:
# __new__ -> for creating object
# __init__ -> for initialize object (setting values)

# If both __init__ method and __new__ method exists in the class, then the __new__ method is executed first and decides
# whether to use __init__ method or not, because other class constructors can be called by __new__ method or it can simply
# return other objects as an instance of this class.


# Example 01
class A:
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init is called")


A()
# Output will be:
#   Creating instance
#   is called


# Below example shows that if the super is omitted for __new__ method the __init__ method will not be executed.
# Let’s see if that is the case.

# Example 02
class A:
    def __new__(cls):
        print("Creating instance")

    # It is not called
    def __init__(self):
        print("Init is called")


A()
# Output will be:
#   Creating instance

# In the above example, it can be seen that __init__ method is not called
# because the constructor is not returning anything


# Example 03
# Below example shows what happens if both the __new__ and __init__ methods are returning something
class A:
    # new method returning a string
    def __new__(cls):
        print("Creating instance")
        return "magic methods"


class B:
    # init method returning a string
    def __init__(self):
        print("Initializing instance")
        return "magic methods"


print(A())
print(B())
# Output will be:
#   Creating instance
#   magic methods
#   Initializing instance
#   B()
#   TypeError: __init__() should return None, not 'str'

# In the above example, it wouldn’t even make sense to return anything from __init__ method
# since it’s purpose is just to alter the fresh state of the newly created instance.


# Example 04
# In the below example we see what happens when we return object from other class
class A:
    def __str__(self):
        return "A object"


class B:
    def __new__(cls):
        return A()

    def __init__(self):
        print("Inside init")


print(B())
# Output will be:
#   A object

# As output shows, __init__ function of the B class isn't called !!!
