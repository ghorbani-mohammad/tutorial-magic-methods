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
class A():
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init is called")

A()