"""
Make class Product callable by def __call__.
"""
__version__ = '3.0.0'
__author__ = "John Q. Wang"
__mydunder__ = "Just a test"
nothing = 'Nothing important'

class Product: 
    def __init__(self): 
        print("Product instance Created") 
  
    # Defining __call__ method 
    def __call__(self, a, b): 
        print(f"{a} x {b} = {a * b}") 

if __name__ == '__main__':

    # Instance created 
    add = Product() 
    
    # __call__ method will be called 
    add(10, 20) 