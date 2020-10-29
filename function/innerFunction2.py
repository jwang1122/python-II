"""
return inner function
"""
def hello():  
    def hi():  
        print("Hello")  
    return hi  

if(__name__ == "__main__"):
    new = hello()  # assign inner function to another function named: new
    new()  