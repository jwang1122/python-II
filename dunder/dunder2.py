class Example: 
    def __init__(self): 
        print("Instance Created") 
      
    # Defining __call__ method 
    def __call__(self, number): 
        print(f"Instance is called via special method with argument {number}") 
  
# Instance created 
e = Example() 
  
# __call__ method will be called 
e(11) 